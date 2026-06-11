import re
import os

workspace_dir = '/Users/sebastianlilliecreutz/Downloads/Home - Golfyr_files/About us - Golfyr_files'

# Let's search inside main.js and sliders.js for specific swiper classes or names
targets = [
    'simpleSliderTimelineV2',
    'simpleSliderTabNav',
    'simpleSliderMakers'
]

for filename in ['main.js', 'sliders.js']:
    filepath = os.path.join(workspace_dir, filename)
    if not os.path.exists(filepath):
        continue
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    print(f"\n==================== FILE: {filename} ====================")
    for tar in targets:
        print(f"--- Target: {tar} ---")
        idx = 0
        while True:
            idx = content.find(tar, idx)
            if idx == -1:
                break
            
            # Print from 200 chars before to 1500 chars after
            start = max(0, idx - 300)
            # Balance curly braces
            brace_count = 0
            end = -1
            brace_started = False
            for j in range(idx, len(content)):
                char = content[j]
                if char == '{':
                    brace_count += 1
                    brace_started = True
                elif char == '}':
                    brace_count -= 1
                    if brace_started and brace_count == 0:
                        end = j + 1
                        break
            if end == -1:
                end = min(len(content), idx + 1000)
            
            print(f"Context (chars {idx}):\n{content[start:end+100]}")
            print("-" * 50)
            idx = end + 1
