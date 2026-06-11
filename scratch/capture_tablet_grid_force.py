import subprocess
import os

seven_file = '/Users/sebastianlilliecreutz/Downloads/Home - Golfyr_files/sevenclubgame.html'
temp_file = '/Users/sebastianlilliecreutz/Downloads/Home - Golfyr_files/temp_tablet_grid_force.html'
artifact_dir = '/Users/sebastianlilliecreutz/.gemini/antigravity/brain/b15a35fe-c2ee-485e-bc8c-5ee93ec01292'

def capture_grid_force(width, height, name):
    # We inject CSS overrides to force all elements to be visible,
    # and a synchronous script to scroll to the #shop element.
    inject_html = """
    <style>
    * {
        opacity: 1 !important;
        visibility: visible !important;
        transition: none !important;
        animation: none !important;
    }
    </style>
    <script>
    const el = document.getElementById('shop');
    if (el) {
        el.scrollIntoView();
    }
    </script>
    """
    with open(seven_file, 'r', encoding='utf-8') as f:
        html = f.read()
    html = html.replace('</body>', inject_html + '\n</body>')
    with open(temp_file, 'w', encoding='utf-8') as f:
        f.write(html)
        
    out_img = os.path.join(artifact_dir, f"{name}.png")
    cmd = [
        "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
        "--headless",
        "--disable-gpu",
        f"--screenshot={out_img}",
        f"--window-size={width},{height}",
        "--virtual-time-budget=2000",
        f"file://{temp_file}"
    ]
    subprocess.run(cmd)
    if os.path.exists(temp_file):
        os.remove(temp_file)
    print(f"Captured {name} to {out_img}")

# Capture tablet
capture_grid_force(768, 1200, "sevenclubgame_tablet_grid_forced")
