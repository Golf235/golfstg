import subprocess
import os
import time
import shutil

index_file = '/Users/sebastianlilliecreutz/Downloads/Home - Golfyr_files/index.html'
seven_file = '/Users/sebastianlilliecreutz/Downloads/Home - Golfyr_files/sevenclubgame.html'
artifact_dir = '/Users/sebastianlilliecreutz/.gemini/antigravity/brain/b15a35fe-c2ee-485e-bc8c-5ee93ec01292'

temp_html_index = '/Users/sebastianlilliecreutz/Downloads/Home - Golfyr_files/temp_clean_index.html'
temp_html_seven = '/Users/sebastianlilliecreutz/Downloads/Home - Golfyr_files/temp_clean_seven.html'

def prepare_and_capture(src, dest, page_name, scroll_y):
    for slide_idx in [0, 1]:
        # Inject script to scroll to specific offset and slide to index
        inject_js = """
        <script>
        window.addEventListener('load', () => {
            setTimeout(() => {
                window.scrollTo(0, """ + str(scroll_y) + """);
                const swiperEl = document.querySelector('.swiper-map-desktop-info');
                if (swiperEl && swiperEl.swiper) {
                    swiperEl.swiper.slideTo(""" + str(slide_idx) + """, 0);
                }
            }, 500);
        });
        </script>
        """
        with open(src, 'r', encoding='utf-8') as f:
            html = f.read()
        html = html.replace('</body>', inject_js + '\n</body>')
        with open(dest, 'w', encoding='utf-8') as f:
            f.write(html)
            
        out_img = os.path.join(artifact_dir, f"clean_{page_name}_slide_{slide_idx + 1}.png")
        cmd = [
            "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
            "--headless",
            "--disable-gpu",
            f"--screenshot={out_img}",
            "--window-size=1200,900",
            f"file://{dest}"
        ]
        try:
            subprocess.run(cmd, timeout=8, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        except subprocess.TimeoutExpired:
            pass
        print(f"Captured {page_name} slide {slide_idx + 1} to {out_img}")
        
    if os.path.exists(dest):
        os.remove(dest)

print("Capturing index.html map (scroll y = 2250)...")
prepare_and_capture(index_file, temp_html_index, "index", 2250)
print("Capturing sevenclubgame.html map (scroll y = 1250)...")
prepare_and_capture(seven_file, temp_html_seven, "sevenclubgame", 1250)


