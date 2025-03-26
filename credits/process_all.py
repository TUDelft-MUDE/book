import yaml
from pathlib import Path
from config import *

# Load the table of contents information from the YAML file
with TOC_FILE.open() as file:
    toc_data = yaml.safe_load(file)
with TOC_FILE_CREDITS.open() as file:
    toc_credits_data = yaml.safe_load(file)

# Load the credits information from the YAML file
with CREDITS_INFO.open() as file:
    credits_data = yaml.safe_load(file)

# Write the credits information to the markdown file as a bullet list
with SUMMARY_FILE.open('w') as file:
    for i, item in enumerate(credits_data['sources']):
        file.write(f"{i + 1}. {item['title']} by {', '.join(item['authors'])}\n")