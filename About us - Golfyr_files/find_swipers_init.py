import re
import os

workspace_dir = '/Users/sebastianlilliecreutz/Downloads/Home - Golfyr_files/About us - Golfyr_files'

files = ['main.js', 'sliders.js']

# Look for 'new Swiper' or Swiper constructor calls, and print the matching block.
for filename in files:
    filepath = os.path.join(workspace_dir, filename)
    if not os.path.exists(filepath):
        continue
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    print(f"\n=== FILE: {filename} ===")
    
    # Search for Swiper instantiation
    # Find all indices of 'new Swiper'
    pos = 0
    while True:
        pos = content.find('new Swiper', pos)
        if pos == -1:
            break
        # Print lines around it
        start_line = content.rfind('\n', 0, pos)
        # Find matching curly braces to print the full instantiation block
        brace_count = 0
        end_pos = -1
        for idx in range(pos, len(content)):
            char = content[idx]
            if char == '{':
                brace_count += 1
            elif char == '}':
                brace_count -= 1
                if brace_count == 0:
                    end_pos = idx + 1
                    break
        if end_pos != -1:
            snippet = content[start_line:end_pos + 50]
            print(f"Match found:\n{snippet}\n" + "-"*40)
            pos = end_pos
        else:
            pos += 10
