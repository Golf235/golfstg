import subprocess
import os
import json
import time
import shutil

src_file = '/Users/sebastianlilliecreutz/Downloads/Home - Golfyr_files/sevenclubgame.html'
dest_file = '/Users/sebastianlilliecreutz/Downloads/Home - Golfyr_files/diag_local_temp.html'
json_output = '/Users/sebastianlilliecreutz/Downloads/Home - Golfyr_files/scratch/diag_local_output.json'
user_data_dir = '/Users/sebastianlilliecreutz/Downloads/Home - Golfyr_files/scratch/chrome_profile_local_diag'

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
    console.log("DIAGNOSTIC: Page loaded.");
    setTimeout(() => {
        try {
            const data = { steps: [] };
            const swiperEl = document.querySelector('.swiper-map-desktop-info');
            data.swiper_exists = !!swiperEl;
            
            data.Swiper_global_exists = typeof Swiper !== 'undefined';
            
            if (swiperEl && swiperEl.swiper) {
                data.swiper_initialized = true;
                
                // Helper function to capture current state
                function captureState(stepName) {
                    const slides = [];
                    swiperEl.querySelectorAll('.swiper-slide').forEach((slide, idx) => {
                        const rect = slide.getBoundingClientRect();
                        const computedStyle = window.getComputedStyle(slide);
                        
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
                            opacity: computedStyle.opacity,
                            display: computedStyle.display,
                            visibility: computedStyle.visibility,
                            title_text: title ? title.innerText : null,
                            title_visible: title ? (window.getComputedStyle(title).visibility !== 'hidden' && window.getComputedStyle(title).display !== 'none') : false,
                            desc_text: desc ? desc.innerText : null
                        });
                    });
                    data.steps.push({
                        step: stepName,
                        active_index: swiperEl.swiper.activeIndex,
                        slides: slides
                    });
                }
                
                captureState("initial");
                
                // Transition to slide index 1 (The Mover)
                swiperEl.swiper.slideTo(1, 0);
                
                setTimeout(() => {
                    captureState("slide_1");
                    
                    // Transition to slide index 3 (The Pitcher)
                    swiperEl.swiper.slideTo(3, 0);
                    
                    setTimeout(() => {
                        captureState("slide_3");
                        console.log("DIAGNOSTIC_DATA_START:" + JSON.stringify(data) + ":DIAGNOSTIC_DATA_END");
                    }, 200);
                }, 200);
                
            } else {
                data.swiper_initialized = false;
                data.swiper_object_exists = !!(swiperEl && swiperEl.swiper);
                console.log("DIAGNOSTIC_DATA_START:" + JSON.stringify(data) + ":DIAGNOSTIC_DATA_END");
            }
            
        } catch (e) {
            console.log("Diagnostic error: " + e.message + " " + e.stack);
        }
    }, 1500);
});
</script>
"""

with open(src_file, 'r', encoding='utf-8') as f:
    html = f.read()

# Replace CDN Swiper with local paths
html = html.replace('https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.css', './swiper-bundle.min.css')
html = html.replace('https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.js', './swiper-bundle.min.js')

# Inject the script just before </body>
html_injected = html.replace('</body>', diagnostic_js + '\n</body>')

with open(dest_file, 'w', encoding='utf-8') as f:
    f.write(html_injected)

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

print("Running headless Chrome to execute diagnostics on local copy...")
try:
    subprocess.run(cmd, timeout=6, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
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
    print("\nDiagnostics completed successfully. Output written to diag_local_output.json.")
else:
    print("\nCould not retrieve diagnostic data from chrome_debug.log.")

if os.path.exists(dest_file):
    os.remove(dest_file)
shutil.rmtree(user_data_dir, ignore_errors=True)
