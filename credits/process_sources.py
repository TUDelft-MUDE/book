import yaml
from pathlib import Path
from config import *



def load_sources(credits_file=CREDITS):
    with credits_file.open() as file:
        credits_data = yaml.safe_load(file)

    sources = credits_data['sources']

    keys_required = ['author',
                     'license',
                     'type']
    keys_optional = ['title',
                     'status',
                     'note',
                     'acknowledgement']

    for s in sources:
        sources[s]['keys_missing'] = []
        sources[s]['keys_set_to_none'] = []
        for k in keys_required:
            if k not in sources[s].keys():
                sources[s]['keys_missing'].append(k)
                print(f"ERROR: no entry for key {k} in source {s}")
        for k in keys_optional:
            if k not in sources[s].keys():
                sources[s]['keys_set_to_none'].append(k)
                sources[s][k] = None
    
    return sources

        

def summarize_sources(output_sources=Path.joinpath(OUTPUT, SUMMARY_OF_SOURCES)):
    sources = load_sources()

    sources_summary = "Summary of Individual Sources\n"
    
    for s in sources.keys():
        sources_summary += "================================================\n"
        sources_summary += f"{s}\n"
        sources_summary += f"    title: {sources[s]['title']}\n"
        sources_summary += f"    authors: {', '.join(sources[s]['author'])}\n"
        sources_summary += f"    keys_missing: {sources[s]['keys_missing']}\n"
        sources_summary += f"    keys_set_to_none: {sources[s]['keys_set_to_none']}\n"
        sources_summary += f"    note:\n{sources[s]['note']}\n"
    sources_summary += "================================================\n"
    with output_sources.open('w') as file:
        file.write(sources_summary)