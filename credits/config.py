from pathlib import Path

# Configuration
OUTPUT = Path("./credits/output")
CREDITS_INFO = Path("./book/_credits.yml")
SUMMARY_FILE = Path.joinpath(OUTPUT, "summary.md")
TOC_FILE = Path("./book/_toc.yml")
TOC_FILE_CREDITS = Path("./credits/_toc_credits.yml")