
"""
Topic 7: File Handling
-----------------------------------------
Theory:
- Open file: open(path, mode)
  modes: 'r' read, 'w' write (overwrite), 'a' append, 'b' binary
- Always close the file (best via 'with' context manager).
- Read methods: read(), readline(), readlines()
- Write methods: write(), writelines()
- Paths: use pathlib for safer cross-platform paths.
- JSON read/write for structured data.
"""

from pathlib import Path
import json

base = Path("./demo_files")
base.mkdir(exist_ok=True)

# Write text file
text_path = base / "notes.txt"
with text_path.open("w", encoding="utf-8") as f:
    f.write("Hello file!\nLine 2\n")

# Read text file
with text_path.open("r", encoding="utf-8") as f:
    content = f.read()
print("Text content:", repr(content))

# Append
with text_path.open("a", encoding="utf-8") as f:
    f.write("Appended line\n")

# Read line by line
with text_path.open() as f:
    for line_no, line in enumerate(f, start=1):
        print(f"{line_no}: {line.strip()}")

# JSON file
data = {"user":"drishti", "score": 99, "skills": ["python", "security"]}
json_path = base / "data.json"
with json_path.open("w", encoding="utf-8") as f:
    json.dump(data, f, indent=2)

with json_path.open() as f:
    loaded = json.load(f)
print("Loaded JSON:", loaded)
