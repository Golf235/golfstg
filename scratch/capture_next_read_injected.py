import subprocess
import os
import time

artifact_dir = "/Users/sebastianlilliecreutz/.gemini/antigravity/brain/00c058d7-0cf7-40a5-a981-9072e1fedae8"
html_dir = "/Users/sebastianlilliecreutz/Downloads/Home - Golfyr_files"
chrome_path = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

pages = [
    ("tech_desktop_nextread_bottom.png", "technology.html", 1440, 900),
    ("tech_mobile_nextread_bottom.png", "technology.html", 390, 800),
    ("innovation_desktop_nextread_bottom.png", "innovation.html", 1440, 900),
    ("innovation_mobile_nextread_bottom.png", "innovation.html", 390, 800),
    ("material_desktop_nextread_bottom.png", "material.html", 1440, 900),
    ("material_mobile_nextread_bottom.png", "material.html", 390, 800),
    ("production_desktop_nextread_bottom.png", "production.html", 1440, 900),
    ("production_mobile_nextread_bottom.png", "production.html", 390, 800)
]

for filename, html_name, width, height in pages:
    src_path = os.path.join(html_dir, html_name)
    temp_name = f"temp_screenshot_{html_name}"
    temp_path = os.path.join(html_dir, temp_name)
    
    # Inject JS to set language to English and scroll to #next-read element
    inject_js = """
    <script>
    localStorage.setItem('selectedLanguage', 'en');
    window.addEventListener('load', () => {
        setTimeout(() => {
            const nextRead = document.getElementById('next-read');
            if (nextRead) {
                nextRead.scrollIntoView({ behavior: 'instant', block: 'start' });
            }
        }, 1000);
    });
    </script>
    """
    
    with open(src_path, 'r', encoding='utf-8') as f:
        html_content = f.read()
        
    html_content = html_content.replace('</body>', inject_js + '\n</body>')
    
    with open(temp_path, 'w', encoding='utf-8') as f:
        f.write(html_content)
        
    dest_path = os.path.join(artifact_dir, filename)
    url = f"file://{temp_path}"
    
    cmd = [
        chrome_path,
        "--headless",
        "--disable-gpu",
        f"--screenshot={dest_path}",
        f"--window-size={width},{height}",
        "--virtual-time-budget=4000",
        url
    ]
    
    print(f"Capturing {filename} ({width}x{height}) using injected scroll...")
    try:
        subprocess.run(cmd, timeout=12, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except subprocess.TimeoutExpired:
        print(f"Timeout expired for {filename}")
        
    if os.path.exists(temp_path):
        os.remove(temp_path)

print("All screenshots captured.")
