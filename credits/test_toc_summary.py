import yaml
from pathlib import Path
from config import *
from process_toc import summarize_toc

# Load the table of contents information from the YAML file
with TOC_FILE_CREDITS.open() as file:
    toc_data = yaml.safe_load(file)

print(f"Processing file {TOC_FILE}:\n")
for key in toc_data.keys():
    print(f"- {key:12} \tlength: {len(toc_data[key])}")
print(f"First part has these keys:\n")
for key in toc_data['parts'][0].keys():
    print(f"- {key:12}")
print(f"First chapter has these keys:")
for c in toc_data['parts'][0]['chapters']:
    print(f"- {c.keys()}")
print(f"First section has these keys:")
for s in toc_data['parts'][0]['chapters'][0]['sections']:
    print(f"- {s.keys()}")
print(f"First section has these files:")
for f in toc_data['parts'][0]['chapters'][0]['sections']:
    print(f"- {f['file']}")

output_file_toc = Path.joinpath(OUTPUT, SUMMARY_OF_TOC_FILES)
summarize_toc(toc_data, output_file_toc)