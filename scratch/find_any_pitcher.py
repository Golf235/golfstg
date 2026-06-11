import os

root_dir = "/Users/sebastianlilliecreutz/Downloads"
for root, dirs, files in os.walk(root_dir):
    # limit depth to 3
    depth = root[len(root_dir):].count(os.sep)
    if depth > 3:
        continue
    for name in dirs + files:
        if "pitcher" in name.lower() or "ptcher" in name.lower():
            print(f"Found match: {os.path.join(root, name)}")
