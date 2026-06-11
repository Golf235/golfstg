import os

files_to_update = [
    "butler.html",
    "index.html",
    "maker.html",
    "mover.html",
    "opener.html",
    "pitcher.html",
    "riser.html"
]

for filename in files_to_update:
    if not os.path.exists(filename):
        print(f"{filename} not found. Skipping.")
        continue
    
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()
        
    updated = content
    updated = updated.replace('href="./index.html#saver"', 'href="./saver.html"')
    updated = updated.replace('href="#saver"', 'href="./saver.html"')
    
    if updated != content:
        with open(filename, "w", encoding="utf-8") as f:
            f.write(updated)
        print(f"Updated links in {filename}")
    else:
        print(f"No links changed in {filename}")

print("Site-wide Saver links updated successfully!")
