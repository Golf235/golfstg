import re

def print_context(filepath, keyword):
    print(f"\n--- Context for '{keyword}' ---")
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    lines = content.splitlines()
    for idx, line in enumerate(lines):
        if keyword.lower() in line.lower():
            start = max(0, idx - 4)
            end = min(len(lines), idx + 8)
            print(f"Match found at line {idx+1}:")
            for i in range(start, end):
                marker = ">>> " if i == idx else "    "
                print(f"{marker}{i+1}: {lines[i]}")

print_context("/Users/sebastianlilliecreutz/Downloads/Home - Golfyr_files/scratch/butler_en.html", "all-round companion")
print_context("/Users/sebastianlilliecreutz/Downloads/Home - Golfyr_files/scratch/butler_en.html", "versatile companion")
print_context("/Users/sebastianlilliecreutz/Downloads/Home - Golfyr_files/scratch/butler_en.html", "The Butler is")
print_context("/Users/sebastianlilliecreutz/Downloads/Home - Golfyr_files/scratch/butler_en.html", "Where do I play")
print_context("/Users/sebastianlilliecreutz/Downloads/Home - Golfyr_files/scratch/butler_de.html", "Wo spiele ich")
