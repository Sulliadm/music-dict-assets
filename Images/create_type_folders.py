#!/usr/bin/env python3
"""
Run this script in the directory where you want the folders created.
It will create one subfolder for each type in types_list.json.

Usage:
    python3 create_type_folders.py

The script expects types_list.json to be in the same directory.
"""

import json
import os
import re

def safe_folder_name(name):
    """Convert a type name to a safe folder name."""
    # Replace characters that are invalid in folder names on Windows/Mac/Linux
    name = name.replace("/", " - ")
    name = name.replace("\\", " - ")
    name = re.sub(r'[<>:"|?*]', "", name)
    name = name.strip()
    return name

# Load the types list
script_dir = os.path.dirname(os.path.abspath(__file__))
json_path = os.path.join(script_dir, "types_list.json")

with open(json_path, "r", encoding="utf-8") as f:
    types = json.load(f)

print(f"Found {len(types)} types in types_list.json")
print(f"Creating folders in: {script_dir}")
print()

created = 0
skipped = 0

for type_name in types:
    folder_name = safe_folder_name(type_name)
    folder_path = os.path.join(script_dir, folder_name)

    if os.path.exists(folder_path):
        print(f"  [exists]  {folder_name}")
        skipped += 1
    else:
        os.makedirs(folder_path)
        print(f"  [created] {folder_name}")
        created += 1

print()
print(f"Done: {created} created, {skipped} already existed.")
