import subprocess
import os

seven_file = '/Users/sebastianlilliecreutz/Downloads/Home - Golfyr_files/sevenclubgame.html'
temp_file = '/Users/sebastianlilliecreutz/Downloads/Home - Golfyr_files/temp_tablet_grid.html'
artifact_dir = '/Users/sebastianlilliecreutz/.gemini/antigravity/brain/b15a35fe-c2ee-485e-bc8c-5ee93ec01292'

def capture_grid(width, height, name):
    inject_js = """
    <script>
    const el = document.getElementById('shop');
    if (el) {
        el.scrollIntoView();
    }
    </script>
    """
    with open(seven_file, 'r', encoding='utf-8') as f:
        html = f.read()
    html = html.replace('</body>', inject_js + '\n</body>')
    with open(temp_file, 'w', encoding='utf-8') as f:
        f.write(html)
        
    out_img = os.path.join(artifact_dir, f"{name}.png")
    cmd = [
        "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
        "--headless",
        "--disable-gpu",
        f"--screenshot={out_img}",
        f"--window-size={width},{height}",
        "--virtual-time-budget=3000",
        f"file://{temp_file}"
    ]
    subprocess.run(cmd)
    if os.path.exists(temp_file):
        os.remove(temp_file)
    print(f"Captured {name} to {out_img}")

# Capture tablet
capture_grid(768, 1200, "sevenclubgame_tablet_grid_before")
# Capture desktop
capture_grid(1200, 1200, "sevenclubgame_desktop_grid_before")
