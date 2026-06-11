import subprocess
import time
import os
import urllib.parse

with open('/Users/sebastianlilliecreutz/Downloads/Home - Golfyr_files/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Clean old screenshots
for i in range(1, 8):
    if os.path.exists(f'slide_{i}.png'):
        os.remove(f'slide_{i}.png')

for step in range(1, 8):
    # We inject a script that automatically scrolls to the swiper section AND slides to the step on load
    inject_slide_to = """
    <script>
    window.addEventListener('load', () => {
        setTimeout(() => {
            const swiperEl = document.querySelector('.swiper-map-desktop-info');
            if (swiperEl && swiperEl.swiper) {
                swiperEl.swiper.slideTo(INDEX_PLACEHOLDER, 0);
            }
            const sec = document.getElementById('sevenclubgame');
            if (sec) {
                sec.scrollIntoView();
            }
        }, 500);
    });
    </script>
    """.replace('INDEX_PLACEHOLDER', str(step - 1))
    
    step_html = content.replace('</body>', inject_slide_to + '\n</body>')
    temp_file = f'/Users/sebastianlilliecreutz/Downloads/Home - Golfyr_files/test_step_{step}.html'
    with open(temp_file, 'w', encoding='utf-8') as f:
        f.write(step_html)
    
    # URL encode the file path for Chrome
    encoded_path = urllib.parse.quote(temp_file)
    url = f"file://{encoded_path}"
    
    cmd = [
        "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
        "--headless",
        "--disable-gpu",
        f"--screenshot=slide_{step}.png",
        "--window-size=1200,1000",
        "--virtual-time-budget=2000",  # Allow 2 seconds of virtual execution time for Swiper/CSS to load
        url
    ]
    print(f"Capturing slide {step} from URL: {url}")
    subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    # clean up step file
    os.remove(temp_file)

print("All screenshots captured!")
