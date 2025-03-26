import yaml
from pathlib import Path
from config import *
from process_sources import *

sources = load_sources()

for s in sources.keys():
    print(f"source: {s}")
    print(f"    note has type: {type(sources[s]['note'])}")
    print(f"    note:\n{sources[s]['note']}")

summarize_sources()