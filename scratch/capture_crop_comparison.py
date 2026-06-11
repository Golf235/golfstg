import subprocess
import os
from PIL import Image

index_file = '/Users/sebastianlilliecreutz/Downloads/Home - Golfyr_files/index.html'
seven_file = '/Users/sebastianlilliecreutz/Downloads/Home - Golfyr_files/sevenclubgame.html'
artifact_dir = '/Users/sebastianlilliecreutz/.gemini/antigravity/brain/b15a35fe-c2ee-485e-bc8c-5ee93ec01292'

temp_html_index = '/Users/sebastianlilliecreutz/Downloads/Home - Golfyr_files/temp_crop_index.html'
temp_html_seven = '/Users/sebastianlilliecreutz/Downloads/Home - Golfyr_files/temp_crop_seven.html'

def capture_and_crop(src, dest, page_name, start_y, end_y):
    # Slide to index 1 (The Mover) on load so we verify transition
    inject_js = """
    <script>
    window.addEventListener('load', () => {
        setTimeout(() => {
            const swiperEl = document.querySelector('.swiper-map-desktop-info');
            if (swiperEl && swiperEl.swiper) {
                swiperEl.swiper.slideTo(1, 0);
            }
        }, 1000);
    });
    </script>
    """
    with open(src, 'r', encoding='utf-8') as f:
        html = f.read()
    html = html.replace('</body>', inject_js + '\n</body>')
    with open(dest, 'w', encoding='utf-8') as f:
        f.write(html)
        
    full_img = os.path.join(artifact_dir, f"full_{page_name}.png")
    cmd = [
        "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
        "--headless",
        "--disable-gpu",
        f"--screenshot={full_img}",
        "--window-size=1200,4500",
        "--virtual-time-budget=3000",
        f"file://{dest}"
    ]
    subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    if os.path.exists(full_img):
        img = Image.open(full_img)
        cropped = img.crop((0, start_y, 1200, end_y))
        cropped.save(os.path.join(artifact_dir, f"crop_{page_name}_map.png"))
        # os.remove(full_img)
        print(f"Captured and cropped {page_name} map section to crop_{page_name}_map.png")
    else:
        print(f"Failed to capture full screenshot for {page_name}")
        
    if os.path.exists(dest):
        os.remove(dest)

print("Capturing index.html (cropping y=2100 to y=3300)...")
capture_and_crop(index_file, temp_html_index, "index", 2100, 3300)

print("Capturing sevenclubgame.html (cropping y=2600 to y=3800)...")
capture_and_crop(seven_file, temp_html_seven, "sevenclubgame", 2600, 3800)
