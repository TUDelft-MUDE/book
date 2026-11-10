"""Check external links and show retained warnings near their HTML content."""

import json
import re
from urllib.parse import urlsplit

from docutils import nodes
from requests.exceptions import RequestException
from sphinx.builders.linkcheck import (
    Hyperlink,
    HyperlinkAvailabilityChecker,
    _get_request_headers,
)
from sphinx.util import logging
from sphinx.util import requests
from sphinx.util.nodes import get_node_line

logger = logging.getLogger(__name__)

TEACHBOOKS_REDIRECT = re.compile(
    r"let\s+currentUrl\s*=\s*window\.location\.href\s*;"
    r"[\s\S]*?let\s+urlParts\s*=\s*currentUrl\.split\('/'\)\s*;"
    r"[\s\S]*?let\s+bname\s*=\s*urlParts\[4\]\s*;"
    r"[\s\S]*?let\s+branches\s*=\s*(\[[^\]]*\])\s*;"
    r"[\s\S]*?if\s*\(\s*!branches\.includes\(bname\)\s*\)\s*\{"
    r"[\s\S]*?urlParts\.splice\(4,\s*0,\s*'([A-Za-z0-9._-]+)'\)\s*;"
    r"[\s\S]*?let\s+newUrl\s*=\s*urlParts\.join\('/'\)\s*;"
    r"[\s\S]*?window\.location\.href\s*=\s*newUrl\s*;"
)


def teachbooks_redirect(uri, html):
    for script in re.findall(r"<script\b[^>]*>([\s\S]*?)</script\s*>", html, re.I):
        match = TEACHBOOKS_REDIRECT.search(script)
        if not match:
            continue
        try:
            branches = json.loads(match.group(1))
        except ValueError:
            continue
        if not isinstance(branches, list) or not all(
            isinstance(branch, str) for branch in branches
        ):
            continue
        parts = uri.split("/")
        if len(parts) < 4 or (len(parts) > 4 and parts[4] in branches):
            return None
        parts.insert(4, match.group(2))
        return "/".join(parts)
    return None


def find_teachbooks_redirect(app, uri):
    headers = _get_request_headers(uri, app.config.linkcheck_request_headers)
    auth = next(
        (value for pattern, value in app.config.linkcheck_auth if re.match(pattern, uri)),
        None,
    )
    with requests.get(
        uri,
        headers=headers,
        auth=auth,
        timeout=app.config.linkcheck_timeout,
        stream=True,
        _user_agent=app.config.user_agent,
        _tls_info=(app.config.tls_verify, app.config.tls_cacerts),
    ) as response:
        if response.status_code != 404:
            return None
        content = bytearray()
        for chunk in response.iter_content(chunk_size=8192):
            content.extend(chunk)
            if len(content) > 262144:
                return None
        url = response.url
        original_fragment = urlsplit(uri).fragment
        if original_fragment and not urlsplit(url).fragment:
            url += "#" + original_fragment
        return teachbooks_redirect(url, content.decode(response.encoding or "utf-8", errors="replace"))


def report_warning(result, message, subtype):
    logger.warning(
        message,
        location=(result.docname, result.lineno),
        type="html_linkcheck",
        subtype=subtype,
    )


def warning_block(node):
    containers = (
        nodes.document, nodes.section, nodes.list_item, nodes.entry,
        nodes.field_body, nodes.definition, nodes.block_quote, nodes.Admonition,
        nodes.container, nodes.topic, nodes.sidebar, nodes.footnote, nodes.citation,
    )
    while node.parent is not None and not isinstance(node.parent, containers):
        node = node.parent
    return node


def check_document_links(app, doctree, docname):
    if not app.config.html_linkcheck_enabled or app.builder.format != "html":
        return

    hyperlinks = {}
    occurrences = []
    for node in doctree.findall():
        uri = None
        if isinstance(node, nodes.reference):
            uri = node.get("refuri")
        elif isinstance(node, nodes.image):
            uri = node.get("candidates", {}).get("?")
        elif isinstance(node, nodes.raw):
            uri = node.get("source")

        if not uri or not uri.startswith(("http://", "https://")):
            continue

        uri = app.emit_firstresult("linkcheck-process-uri", uri) or uri
        try:
            line = get_node_line(node)
        except ValueError:
            line = -1
        hyperlink = Hyperlink(uri, docname, app.env.doc2path(docname), line)
        hyperlinks.setdefault(uri, hyperlink)
        occurrences.append((node, hyperlink))

    if not hyperlinks:
        return

    results_by_uri = app.html_linkcheck_results
    unchecked = {
        uri: hyperlink
        for uri, hyperlink in hyperlinks.items()
        if uri not in results_by_uri
    }
    redirects = {}
    new_results = (
        HyperlinkAvailabilityChecker(app.config).check(unchecked) if unchecked else ()
    )
    for result in new_results:
        if result.status == "broken":
            target = None
            if result.message.startswith("404 Client Error:"):
                try:
                    target = find_teachbooks_redirect(app, result.uri)
                except RequestException as error:
                    results_by_uri[result.uri] = (
                        "incomplete",
                        f"LINK CHECK INCOMPLETE: {result.uri} "
                        f"(could not inspect 404 response: {error})",
                    )
                    continue
            if target:
                redirects.setdefault(target, []).append(result)
            else:
                results_by_uri[result.uri] = (
                    "broken",
                    f"BROKEN LINK: {result.uri} ({result.message})",
                )
        elif result.status in ("timeout", "unknown", ""):
            results_by_uri[result.uri] = (
                "incomplete",
                f"LINK CHECK INCOMPLETE: {result.uri} "
                f"({result.message or result.status or 'unknown status'})",
            )
        else:
            results_by_uri[result.uri] = None

    if redirects:
        redirect_hyperlinks = {
            target: Hyperlink(
                target, results[0].docname, app.env.doc2path(results[0].docname),
                results[0].lineno,
            )
            for target, results in redirects.items()
        }
        for result in HyperlinkAvailabilityChecker(app.config).check(redirect_hyperlinks):
            for original in redirects[result.uri]:
                if result.status == "broken":
                    results_by_uri[original.uri] = (
                        "broken",
                        f"BROKEN LINK: {original.uri} "
                        f"(TeachBooks redirect to {result.uri}: {result.message})",
                    )
                elif result.status not in ("working", "redirected"):
                    results_by_uri[original.uri] = (
                        "incomplete",
                        f"LINK CHECK INCOMPLETE: {original.uri} "
                        f"(TeachBooks redirect to {result.uri}: "
                        f"{result.message or result.status or 'unknown status'})",
                    )
                else:
                    results_by_uri[original.uri] = None

    if app.config.keep_warnings:
        last_warnings = {}
        for node, hyperlink in occurrences:
            cached_result = results_by_uri[hyperlink.uri]
            if cached_result is None:
                continue
            block = warning_block(node)
            block_key = id(block)
            _, message = cached_result
            warning = nodes.system_message(
                message,
                type="WARNING",
                level=2,
                source=app.env.doc2path(hyperlink.docname),
                line=hyperlink.lineno,
            )
            previous = last_warnings.get(block_key, block)
            previous.parent.insert(previous.parent.index(previous) + 1, warning)
            last_warnings[block_key] = warning

    for uri, hyperlink in hyperlinks.items():
        cached_result = results_by_uri[uri]
        if cached_result is not None:
            subtype, message = cached_result
            report_warning(hyperlink, message, subtype)


def setup(app):
    app.add_config_value("html_linkcheck_enabled", True, "html", types=[bool])
    app.html_linkcheck_results = {}
    app.connect("doctree-resolved", check_document_links)
    return {"parallel_read_safe": True, "parallel_write_safe": False}
