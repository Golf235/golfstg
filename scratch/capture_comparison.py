import subprocess
import os
import time
import shutil

index_file = '/Users/sebastianlilliecreutz/Downloads/Home - Golfyr_files/index.html'
seven_file = '/Users/sebastianlilliecreutz/Downloads/Home - Golfyr_files/sevenclubgame.html'
artifact_dir = '/Users/sebastianlilliecreutz/.gemini/antigravity/brain/b15a35fe-c2ee-485e-bc8c-5ee93ec01292'

temp_html_index = '/Users/sebastianlilliecreutz/Downloads/Home - Golfyr_files/temp_capture_index.html'
temp_html_seven = '/Users/sebastianlilliecreutz/Downloads/Home - Golfyr_files/temp_capture_seven.html'

def prepare_and_capture(src, dest, page_name):
    # Inject JS to slide to specific index on load and then take screenshot
    for slide_idx in [0, 1, 2, 3]:
        inject_js = """
        <script>
        window.addEventListener('load', () => {
            setTimeout(() => {
                const swiperEl = document.querySelector('.swiper-map-desktop-info');
                if (swiperEl && swiperEl.swiper) {
                    swiperEl.swiper.slideTo(""" + str(slide_idx) + """, 0);
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
            
        out_img = os.path.join(artifact_dir, f"{page_name}_slide_{slide_idx + 1}.png")
        cmd = [
            "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
            "--headless",
            "--disable-gpu",
            f"--screenshot={out_img}",
            "--window-size=1200,900",
            "--virtual-time-budget=2000",
            f"file://{dest}#sevenclubgame"
        ]
        subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(f"Captured {page_name} slide {slide_idx + 1} to {out_img}")
        
    if os.path.exists(dest):
        os.remove(dest)

print("Capturing index.html slides...")
prepare_and_capture(index_file, temp_html_index, "index")
print("Capturing sevenclubgame.html slides...")
prepare_and_capture(seven_file, temp_html_seven, "sevenclubgame")
