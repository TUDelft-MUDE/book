from pathlib import Path
import yaml

CREDITS_INFO = Path("./book/_credits.yml")
CREDITS_FILE = Path("./test.md")

# Load the credits information from the YAML file
with CREDITS_INFO.open() as file:
    credits_data = yaml.safe_load(file)

# Write the credits information to the markdown file as a bullet list
with CREDITS_FILE.open('w') as file:
    for i, item in enumerate(credits_data['sources']):
        file.write(f"{i + 1}. {item['title']} from Week {item['week_number']} by {', '.join(item['authors'])}\n")