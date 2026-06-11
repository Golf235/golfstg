import shutil
import os

src_dir = "/Users/sebastianlilliecreutz/Downloads/Home - Golfyr_files/The Opener - Golfyr_files"
dest_dir = "/Users/sebastianlilliecreutz/.gemini/antigravity/brain/633bc07e-1a63-423a-9de9-ae4a1302a620"

os.makedirs(dest_dir, exist_ok=True)

files_to_copy = [
    "techspecs-opener-loft.png",
    "techspecs-opener-lie.png",
    "techspecs-opener-length.png",
    "techspecs-opener-swing-weight.png"
]

for f in files_to_copy:
    src_path = os.path.join(src_dir, f)
    dest_path = os.path.join(dest_dir, f)
    if os.path.exists(src_path):
        shutil.copy(src_path, dest_path)
        print(f"Copied {f} to artifacts.")
    else:
        print(f"Source file {f} not found.")
