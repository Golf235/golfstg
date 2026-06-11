import subprocess
import os
import urllib.parse
import re

about_path = '/Users/sebastianlilliecreutz/Downloads/Home - Golfyr_files/about.html'

with open(about_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Split HTML into header (up to </header>), main content, and footer (from <footer> to end)
header_match = re.search(r'^(.*?</header>)', html, re.DOTALL)
footer_match = re.search(r'(<footer>.*)$', html, re.DOTALL)

if not header_match or not footer_match:
    print("Could not parse header or footer from about.html!")
    exit(1)

header_html = header_match.group(1)
footer_html = footer_match.group(1)

# Find all section blocks inside <main>
# We can find sections by matching <section ...> to the next <section or </main>
sections = re.findall(r'(<section.*?</section>)', html, re.DOTALL)
print(f"Parsed {len(sections)} sections in about.html")

# Let's define the layouts we want to capture by choosing which sections to include
layouts = [
    ("about_desktop_top.png", 1440, 1200, [0, 1]), # Hero and Intro text (index 0, 1)
    ("about_desktop_intro.png", 1440, 1000, [1, 2]), # Intro text and Values (index 1, 2)
    ("about_desktop_values.png", 1440, 900, [2]), # Values tab swiper (index 2)
    ("about_desktop_timeline.png", 1440, 900, [4]), # Timeline (index 4)
    ("about_desktop_makers.png", 1440, 900, [5, 6, 7, 8]), # Visionaries + Roger Quote + Makers (index 5, 6, 7, 8)
    ("about_desktop_stats.png", 1440, 900, [9, 10]), # Milestones + Stats (index 9, 10)
    ("about_mobile_top.png", 400, 1400, [0, 1]),
    ("about_mobile_intro.png", 400, 1200, [1, 2]), # Intro text and Values (index 1, 2)
    ("about_mobile_values.png", 400, 900, [2]),
    ("about_mobile_timeline.png", 400, 900, [4]),
    ("about_mobile_makers.png", 400, 1600, [5, 6, 7, 8]),
    ("about_tablet_stats.png", 768, 900, [9, 10]),
    ("about_mobile_stats.png", 400, 1600, [9, 10]),
]

for name, width, height, section_indices in layouts:
    # Build content for this verification layout
    layout_content = "\n".join(sections[idx] for idx in section_indices)
    
    # Construct complete HTML
    main_style = ' style="margin-top: 120px;"' if "intro" in name else ""
    temp_html = f"""{header_html}
    <main{main_style}>
    {layout_content}
    </main>
    {footer_html}"""
    
    temp_file = f'/Users/sebastianlilliecreutz/Downloads/Home - Golfyr_files/temp_verify_{name}.html'
    with open(temp_file, 'w', encoding='utf-8') as f:
        f.write(temp_html)
        
    url = f"file://{temp_file}"
    
    cmd = [
        "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
        "--headless",
        "--disable-gpu",
        f"--screenshot={name}",
        f"--window-size={width},{height}",
        "--virtual-time-budget=3000", # Increase virtual time budget to allow assets to load
        url
    ]
    print(f"Capturing {name} ({width}x{height}) with sections {section_indices}...")
    subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    
    # clean up
    if os.path.exists(temp_file):
        os.remove(temp_file)

print("All sections captured successfully!")
