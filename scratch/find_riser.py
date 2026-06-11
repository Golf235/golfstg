import os

root_dir = "/Users/sebastianlilliecreutz/Downloads/Home - Golfyr_files"
for root, dirs, files in os.walk(root_dir):
    for name in dirs + files:
        if "riser" in name.lower():
            print(f"Found match: {os.path.join(root, name)}")
