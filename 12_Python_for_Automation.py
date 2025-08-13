
"""
Topic 12: Python for Automation
-----------------------------------------
Theory:
- File, folder, and system tasks ko automate karo.
- Use: os, pathlib, shutil, subprocess.
- Examples: bulk rename, log parsing, scheduled scripts.
"""

import os, shutil, subprocess
from pathlib import Path

root = Path("./auto_demo")
root.mkdir(exist_ok=True)

# Create some files
for i in range(3):
    (root / f"log_{i}.txt").write_text(f"line {i}\n", encoding="utf-8")

# Bulk rename: add prefix 'processed_'
for p in root.glob("*.txt"):
    p.rename(p.with_name(f"processed_{p.name}"))

print("files after rename:", [p.name for p in root.glob('*')])

# Run a shell command safely (list form) to get directory listing
result = subprocess.run(["python", "--version"], capture_output=True, text=True)
print("python version:", result.stdout or result.stderr)
