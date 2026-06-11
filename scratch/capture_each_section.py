import subprocess
import os
import re

about_path = '/Users/sebastianlilliecreutz/Downloads/Home - Golfyr_files/about.html'

with open(about_path, 'r', encoding='utf-8') as f:
    html = f.read()

header_match = re.search(r'^(.*?</header>)', html, re.DOTALL)
footer_match = re.search(r'(<footer>.*)$', html, re.DOTALL)

if not header_match or not footer_match:
    print("Could not parse header or footer!")
    exit(1)

header_html = header_match.group(1)
footer_html = footer_match.group(1)

sections = re.findall(r'(<section.*?</section>)', html, re.DOTALL)

# Capture Roger Stadler (6), Makers (8), and Marcel (11)
targets = [
    ("roger_section.png", 1440, 700, [6]),
    ("makers_section.png", 1440, 700, [8]),
    ("marcel_section.png", 1440, 700, [11])
]

for name, width, height, indices in targets:
    content = "\n".join(sections[idx] for idx in indices)
    temp_html = f"{header_html}\n<main>\n{content}\n</main>\n{footer_html}"
    temp_file = f'/Users/sebastianlilliecreutz/Downloads/Home - Golfyr_files/temp_capture_{name}.html'
    
    with open(temp_file, 'w', encoding='utf-8') as f:
        f.write(temp_html)
        
    cmd = [
        "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
        "--headless",
        "--disable-gpu",
        f"--screenshot={name}",
        f"--window-size={width},{height}",
        "--virtual-time-budget=3000",
        f"file://{temp_file}"
    ]
    subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    if os.path.exists(temp_file):
        os.remove(temp_file)

print("Generated target screenshots.")
