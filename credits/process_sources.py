import yaml
from pathlib import Path
from config import *



def load_sources(credits_file=CREDITS):
    with credits_file.open() as file:
        credits_data = yaml.safe_load(file)
    return credits_data['sources']

def summarize_sources(output_sources=Path.joinpath(OUTPUT, SUMMARY_OF_SOURCES)):
    sources = load_sources()

    sources_summary = "Summary of Individual Sources\n"
    
    for s in sources.keys():
        sources_summary += "================================================\n"
        sources_summary += f"{s}\n"
        sources_summary += f"    title:{sources[s]['title']}\n"
        sources_summary += f"    authors: {', '.join(sources[s]['authors'])}\n"
    
    sources_summary += "================================================\n"
    with output_sources.open('w') as file:
        file.write(sources_summary)

summarize_sources()