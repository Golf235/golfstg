import os
import re

def get_block_extent(lines, pattern):
    start = -1
    for idx, line in enumerate(lines):
        if re.search(pattern, line):
            start = idx + 1
            break
    if start == -1:
        return -1, -1
    # Find where the block of comments or styles ends by looking for the next major block comment or section
    # Usually in these wordpress-generated main-1920.css files, sections are separated by comments like:
    # /*--------------------------------------------------------------
    # # or similar. Let's look for the next comment or next section or when indentation goes back to 0 after some lines.
    # But since they are defined together, let's find the line index where the next section comment starts.
    end = len(lines)
    for idx in range(start, len(lines)):
        line = lines[idx]
        if line.strip().startswith('/*#') or line.strip().startswith('/*--------------------') or 'Theme-defined sections' in line:
            end = idx
            break
        # Also check if it's the start of another section we care about
        if '.responsive-image-content' in line and pattern != r'\.responsive-image-content':
            # wait, let's just use comments or section dividers
            pass
    return start, end

# Let's inspect the files
workspace_dir = '/Users/sebastianlilliecreutz/Downloads/Home - Golfyr_files/About us - Golfyr_files'

files = ['main-1920.css', 'main-phase-2.css', 'main-phase-3.css', 'sliders.css']
patterns = [
    (r'\.simple-slider-makers\b', 'simple-slider-makers'),
    (r'\.simple-slider-timeline-v2\b', 'simple-slider-timeline-v2'),
    (r'\.numbers-and-data-entry\b', 'numbers-and-data-entry'),
    (r'\.slider-tabs-nav\b', 'slider-tabs-nav'),
    (r'\.quote-with-image\b', 'quote-with-image')
]

for filename in files:
    filepath = os.path.join(workspace_dir, filename)
    if not os.path.exists(filepath):
        continue
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    print(f"\nFile: {filename} ({len(lines)} lines)")
    for pat, name in patterns:
        start = -1
        end = -1
        # Let's find all occurrences of pattern
        occs = [i+1 for i, l in enumerate(lines) if re.search(pat, l)]
        if occs:
            print(f"  {name}: {len(occs)} matches, lines {occs[0]} to {occs[-1]}")
            # Let's guess the range: starts a bit before the first match (if there are comments), and ends a bit after the last match's closing brace.
            # Let's print the lines around the first match to see
            print(f"    Sample: {lines[occs[0]-1].strip()}")
