import subprocess
import os
import json
import shutil

src_file = '/Users/sebastianlilliecreutz/Downloads/Home - Golfyr_files/sevenclubgame.html'
dest_file = '/Users/sebastianlilliecreutz/Downloads/Home - Golfyr_files/diag_transform_temp.html'
user_data_dir = '/Users/sebastianlilliecreutz/Downloads/Home - Golfyr_files/scratch/chrome_profile_transform'

if not os.path.exists(user_data_dir):
    os.makedirs(user_data_dir)

diagnostic_js = """
<script>
window.addEventListener('load', () => {
    setTimeout(() => {
        try {
            const data = { steps: [] };
            const swiperEl = document.querySelector('.swiper-map-desktop-info');
            if (swiperEl && swiperEl.swiper) {
                const wrapper = swiperEl.querySelector('.swiper-wrapper');
                
                function capture(stepName) {
                    const slides = [];
                    swiperEl.querySelectorAll('.swiper-slide').forEach((slide, idx) => {
                        slides.push({
                            index: idx,
                            class: slide.className,
                            style: slide.getAttribute('style') || '',
                            rect: slide.getBoundingClientRect().left
                        });
                    });
                    data.steps.push({
                        step: stepName,
                        activeIndex: swiperEl.swiper.activeIndex,
                        wrapperStyle: wrapper ? wrapper.getAttribute('style') : '',
                        wrapperRect: wrapper ? wrapper.getBoundingClientRect().left : 0,
                        slides: slides
                    });
                }
                
                capture("initial");
                
                swiperEl.swiper.slideTo(1, 0);
                setTimeout(() => {
                    capture("slide_1");
                    
                    swiperEl.swiper.slideTo(3, 0);
                    setTimeout(() => {
                        capture("slide_3");
                        console.log("TRANSFORM_DATA:" + JSON.stringify(data));
                    }, 200);
                }, 200);
            } else {
                console.log("TRANSFORM_DATA:swiper_missing");
            }
        } catch (e) {
            console.log("Error: " + e.message);
        }
    }, 1500);
});
</script>
"""

with open(src_file, 'r', encoding='utf-8') as f:
    html = f.read()
html = html.replace('</body>', diagnostic_js + '\n</body>')
with open(dest_file, 'w', encoding='utf-8') as f:
    f.write(html)

log_file = os.path.join(user_data_dir, 'chrome_debug.log')
if os.path.exists(log_file):
    os.remove(log_file)

cmd = [
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "--headless",
    "--disable-gpu",
    "--window-size=1200,1000",
    f"--user-data-dir={user_data_dir}",
    "--enable-logging",
    "--v=1",
    f"file://{dest_file}"
]

try:
    subprocess.run(cmd, timeout=8, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
except subprocess.TimeoutExpired:
    pass

if os.path.exists(log_file):
    with open(log_file, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    for line in content.split('\n'):
        if "TRANSFORM_DATA:" in line:
            start = line.find("TRANSFORM_DATA:") + len("TRANSFORM_DATA:")
            sub = line[start:]
            first_brace = sub.find("{")
            last_brace = sub.rfind("}")
            if first_brace != -1 and last_brace != -1:
                json_str = sub[first_brace:last_brace+1]
                json_str = json_str.replace('\\"', '"').replace('\\\\', '\\')
                try:
                    data = json.loads(json_str)
                    print(json.dumps(data, indent=2))
                except Exception as e:
                    print("Failed to parse:", e)
else:
    print("Log file missing.")

if os.path.exists(dest_file):
    os.remove(dest_file)
shutil.rmtree(user_data_dir, ignore_errors=True)
