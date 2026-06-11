import subprocess
import os
import json
import time
import shutil

src_file = '/Users/sebastianlilliecreutz/Downloads/Home - Golfyr_files/sevenclubgame.html'
dest_file = '/Users/sebastianlilliecreutz/Downloads/Home - Golfyr_files/scratch/debug_temp.html'
json_output = '/Users/sebastianlilliecreutz/Downloads/Home - Golfyr_files/scratch/map_debug_output.json'
user_data_dir = '/Users/sebastianlilliecreutz/Downloads/Home - Golfyr_files/scratch/chrome_profile_diag'

if os.path.exists(json_output):
    os.remove(json_output)

if not os.path.exists(user_data_dir):
    os.makedirs(user_data_dir)

log_file = os.path.join(user_data_dir, 'chrome_debug.log')
if os.path.exists(log_file):
    os.remove(log_file)

# Diagnostic JS to inject into the page
diagnostic_js = """
<script>
window.addEventListener('load', () => {
    setTimeout(() => {
        try {
            const data = {};
            const swiperEl = document.querySelector('.swiper-map-desktop-info');
            data.swiper_exists = !!swiperEl;
            if (swiperEl) {
                data.swiper_initialized = !!swiperEl.swiper;
                if (swiperEl.swiper) {
                    data.swiper_active_index = swiperEl.swiper.activeIndex;
                    data.swiper_slides_length = swiperEl.swiper.slides.length;
                }
                
                // Get all slides and their computed styles and HTML
                const slides = [];
                swiperEl.querySelectorAll('.swiper-slide').forEach((slide, idx) => {
                    const rect = slide.getBoundingClientRect();
                    const computedStyle = window.getComputedStyle(slide);
                    
                    // Check children
                    const card = slide.querySelector('.info-card');
                    const title = slide.querySelector('.info-card-title');
                    const desc = slide.querySelector('.info-card-desc');
                    
                    slides.push({
                        index: idx,
                        classes: slide.className,
                        rect: {
                            top: rect.top,
                            left: rect.left,
                            width: rect.width,
                            height: rect.height
                        },
                        styles: {
                            opacity: computedStyle.opacity,
                            display: computedStyle.display,
                            visibility: computedStyle.visibility,
                            color: computedStyle.color,
                            backgroundColor: computedStyle.backgroundColor
                        },
                        html: slide.innerHTML.trim().substring(0, 300),
                        card_exists: !!card,
                        title_text: title ? title.innerText : null,
                        title_html: title ? title.innerHTML : null,
                        title_color: title ? window.getComputedStyle(title).color : null,
                        desc_text: desc ? desc.innerText : null
                    });
                });
                data.slides = slides;
            }
            
            // Check global styling variables
            data.body_bg = window.getComputedStyle(document.body).backgroundColor;
            
            // Output to console
            console.log("DIAGNOSTIC_DATA_START:" + JSON.stringify(data) + ":DIAGNOSTIC_DATA_END");
        } catch (e) {
            console.error("Diagnostic error:", e);
        }
    }, 1000);
});
</script>
"""

with open(src_file, 'r', encoding='utf-8') as f:
    html = f.read()

# Inject the script just before </body>
html_injected = html.replace('</body>', diagnostic_js + '\n</body>')

with open(dest_file, 'w', encoding='utf-8') as f:
    f.write(html_injected)

cmd = [
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "--headless",
    "--disable-gpu",
    f"--user-data-dir={user_data_dir}",
    "--enable-logging",
    "--v=1",
    f"file://{dest_file}"
]

print("Running headless Chrome to execute diagnostics...")
try:
    subprocess.run(cmd, timeout=5, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
except subprocess.TimeoutExpired:
    print("Chrome execution finished (timeout reached).")

# Extract JSON from output log
diagnostic_json = None
if os.path.exists(log_file):
    with open(log_file, 'r', encoding='utf-8', errors='ignore') as f:
        log_content = f.read()
    
    print("\n--- CHROME CONSOLE LOGS ---")
    for line in log_content.split('\n'):
        if 'CONSOLE' in line:
            print(line)
        if "DIAGNOSTIC_DATA_START" in line:
            start = line.find("DIAGNOSTIC_DATA_START:") + len("DIAGNOSTIC_DATA_START:")
            end = line.find(":DIAGNOSTIC_DATA_END")
            if start != -1 and end != -1:
                json_str = line[start:end]
                diagnostic_json = json.loads(json_str)

if diagnostic_json:
    with open(json_output, 'w', encoding='utf-8') as f:
        json.dump(diagnostic_json, f, indent=4)
    print("\nDiagnostics completed successfully. Output written to map_debug_output.json.")
else:
    print("\nCould not retrieve diagnostic data from chrome_debug.log.")

if os.path.exists(dest_file):
    os.remove(dest_file)
shutil.rmtree(user_data_dir, ignore_errors=True)
