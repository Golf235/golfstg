import os

files_to_update = [
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
    # Replace the swiper discover button href
    updated = updated.replace('href="./index.html#butler"', 'href="./butler.html"')
    updated = updated.replace('href="#butler"', 'href="./butler.html"')
    
    if updated != content:
        with open(filename, "w", encoding="utf-8") as f:
            f.write(updated)
        print(f"Updated links in {filename}")
    else:
        print(f"No links changed in {filename}")

print("Site-wide links updated successfully!")
