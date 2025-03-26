import yaml
from pathlib import Path
from config import *

def load_sources(credits_file=CREDITS_INFO):
    with credits_file.open() as file:
        credits_data = yaml.safe_load(file)
    return credits_data['sources']

def summarize_sources():
    sources = load_sources()
    with SUMMARY_FILE.open('w') as file:
        for i, item in enumerate(sources):
            file.write(f"{i + 1}. {item['title']} by {', '.join(item['authors'])}\n")

# summarize_sources()