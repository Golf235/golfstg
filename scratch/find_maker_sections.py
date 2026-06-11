import re

def print_context(filepath, keyword):
    print(f"\n--- Context for '{keyword}' ---")
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Let's find matches and show lines around them
    lines = content.splitlines()
    for idx, line in enumerate(lines):
        if keyword.lower() in line.lower():
            start = max(0, idx - 4)
            end = min(len(lines), idx + 8)
            print(f"Match found at line {idx+1}:")
            for i in range(start, end):
                marker = ">>> " if i == idx else "    "
                print(f"{marker}{i+1}: {lines[i]}")

print_context("/Users/sebastianlilliecreutz/Downloads/Home - Golfyr_files/scratch/maker_en.html", "Sergio Garcia")
print_context("/Users/sebastianlilliecreutz/Downloads/Home - Golfyr_files/scratch/maker_en.html", "cool head")
print_context("/Users/sebastianlilliecreutz/Downloads/Home - Golfyr_files/scratch/maker_en.html", "attack the green")
print_context("/Users/sebastianlilliecreutz/Downloads/Home - Golfyr_files/scratch/maker_en.html", "Precision on the Green")
