import subprocess
import os
import json
import shutil

index_file = '/Users/sebastianlilliecreutz/Downloads/Home - Golfyr_files/index.html'
seven_file = '/Users/sebastianlilliecreutz/Downloads/Home - Golfyr_files/sevenclubgame.html'
dest_file_index = '/Users/sebastianlilliecreutz/Downloads/Home - Golfyr_files/diag_index_temp.html'
dest_file_seven = '/Users/sebastianlilliecreutz/Downloads/Home - Golfyr_files/diag_seven_temp.html'

user_data_dir = '/Users/sebastianlilliecreutz/Downloads/Home - Golfyr_files/scratch/chrome_profile_comparison'
if not os.path.exists(user_data_dir):
    os.makedirs(user_data_dir)

# Diagnostic JS to inject
diagnostic_js = """
<script>
window.addEventListener('load', () => {
    setTimeout(() => {
        try {
            const data = {};
            const swiperEl = document.querySelector('.swiper-map-desktop-info');
            if (swiperEl) {
                const rect = swiperEl.getBoundingClientRect();
                const style = window.getComputedStyle(swiperEl);
                data.swiper = {
                    left: rect.left,
                    top: rect.top,
                    width: rect.width,
                    height: rect.height,
                    display: style.display,
                    visibility: style.visibility,
                    opacity: style.opacity
                };
                
                const wrapper = swiperEl.querySelector('.swiper-wrapper');
                if (wrapper) {
                    const wRect = wrapper.getBoundingClientRect();
                    const wStyle = window.getComputedStyle(wrapper);
                    data.wrapper = {
                        left: wRect.left,
                        top: wRect.top,
                        width: wRect.width,
                        height: wRect.height,
                        transform: wStyle.transform
                    };
                }
                
                const slides = [];
                swiperEl.querySelectorAll('.swiper-slide').forEach((slide, idx) => {
                    const sRect = slide.getBoundingClientRect();
                    const sStyle = window.getComputedStyle(slide);
                    const title = slide.querySelector('.info-card-title');
                    const desc = slide.querySelector('.info-card-desc');
                    slides.push({
                        index: idx,
                        classes: slide.className,
                        left: sRect.left,
                        top: sRect.top,
                        width: sRect.width,
                        height: sRect.height,
                        opacity: sStyle.opacity,
                        display: sStyle.display,
                        visibility: sStyle.visibility,
                        title_text: title ? title.innerText : null,
                        desc_text: desc ? desc.innerText : null
                    });
                });
                data.slides = slides;
            } else {
                data.error = "No swiper-map-desktop-info found";
            }
            console.log("COMPARISON_DATA:" + JSON.stringify(data));
        } catch (e) {
            console.log("Diagnostic error: " + e.message);
        }
    }, 1500);
});
</script>
"""

def run_diag(src_path, dest_path):
    with open(src_path, 'r', encoding='utf-8') as f:
        html = f.read()
    html = html.replace('</body>', diagnostic_js + '\n</body>')
    with open(dest_path, 'w', encoding='utf-8') as f:
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
        f"file://{dest_path}"
    ]
    try:
        subprocess.run(cmd, timeout=6, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except subprocess.TimeoutExpired:
        pass
    
    result = None
    if os.path.exists(log_file):
        with open(log_file, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        for line in content.split('\n'):
            if "COMPARISON_DATA:" in line:
                start = line.find("COMPARISON_DATA:") + len("COMPARISON_DATA:")
                # Clean up Chrome console wrapper escape characters
                sub = line[start:]
                # If wrapped in quotes, find the actual json bounds
                first_brace = sub.find("{")
                last_brace = sub.rfind("}")
                if first_brace != -1 and last_brace != -1:
                    json_str = sub[first_brace:last_brace+1]
                    # Chrome logs double escape double-quotes
                    json_str = json_str.replace('\\"', '"').replace('\\\\', '\\')
                    try:
                        result = json.loads(json_str)
                    except Exception as e:
                        print("Failed to parse JSON string:", json_str, e)
    if os.path.exists(dest_path):
        os.remove(dest_path)
    return result

print("Running diagnostics on index.html...")
index_res = run_diag(index_file, dest_file_index)
print("Running diagnostics on sevenclubgame.html...")
seven_res = run_diag(seven_file, dest_file_seven)

print("\n--- RESULTS COMPARISON ---")
print("Index.html Swiper info:")
print(json.dumps(index_res, indent=2))
print("\nSevenclubgame.html Swiper info:")
print(json.dumps(seven_res, indent=2))

shutil.rmtree(user_data_dir, ignore_errors=True)
