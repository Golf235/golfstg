import os

parent_dir = "/Users/sebastianlilliecreutz/Downloads"
for item in os.listdir(parent_dir):
    if "pitcher" in item.lower() or "ptcher" in item.lower():
        print(f"Found match: {item}")
