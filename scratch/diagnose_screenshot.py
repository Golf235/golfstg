import subprocess
import os
import shutil

html_dir = "/Users/sebastianlilliecreutz/Downloads/Home - Golfyr_files"
user_data_dir = "/Users/sebastianlilliecreutz/Downloads/Home - Golfyr_files/chrome_profile_diag"
chrome_path = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

# Make sure user data dir is clean
shutil.rmtree(user_data_dir, ignore_errors=True)
os.makedirs(user_data_dir, exist_ok=True)

# Create a temporary html file with injected scroll JS
src_path = os.path.join(html_dir, "technology.html")
temp_path = os.path.join(html_dir, "temp_diag_tech.html")

inject_js = """
<script>
window.addEventListener('load', () => {
    console.log("DIAG: window load fired");
    setTimeout(() => {
        console.log("DIAG: timeout fired, scrolling");
        const nextRead = document.getElementById('next-read');
        if (nextRead) {
            console.log("DIAG: next-read element found!");
            console.log("DIAG: Before scroll, scrollY=" + window.scrollY);
            console.log("DIAG: Before scroll, rect=" + JSON.stringify(nextRead.getBoundingClientRect()));
            nextRead.scrollIntoView({ behavior: 'instant', block: 'start' });
            console.log("DIAG: scrollIntoView called");
            console.log("DIAG: After scroll, scrollY=" + window.scrollY);
            console.log("DIAG: After scroll, rect=" + JSON.stringify(nextRead.getBoundingClientRect()));
        } else {
            console.error("DIAG ERROR: next-read element NOT found!");
        }
    }, 1000);
});
</script>
"""

with open(src_path, 'r', encoding='utf-8') as f:
    html_content = f.read()
html_content = html_content.replace('</body>', inject_js + '\n</body>')
with open(temp_path, 'w', encoding='utf-8') as f:
    f.write(html_content)

cmd = [
    chrome_path,
    "--headless",
    "--disable-gpu",
    f"--user-data-dir={user_data_dir}",
    "--enable-logging",
    "--v=1",
    f"--screenshot={os.path.join(html_dir, 'scratch/diag_output.png')}",
    "--window-size=1440,900",
    "--virtual-time-budget=4000",
    f"file://{temp_path}"
]

print("Running chrome...")
try:
    res = subprocess.run(cmd, timeout=10, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print("Chrome finished executing. Exit code:", res.returncode)
except subprocess.TimeoutExpired as e:
    print("Chrome timeout expired")

# Read log file
chrome_log = os.path.join(user_data_dir, 'chrome_debug.log')
if os.path.exists(chrome_log):
    with open(chrome_log, 'r', encoding='utf-8', errors='ignore') as f:
        log_content = f.read()
    print("\n--- CHROME LOG CONTENTS ---")
    for line in log_content.split('\n'):
        if 'DIAG' in line or 'CONSOLE' in line or 'Error' in line or 'Failed' in line or 'exception' in line:
            print(line)
else:
    print("chrome_debug.log not found")

# Clean up
if os.path.exists(temp_path):
    os.remove(temp_path)
shutil.rmtree(user_data_dir, ignore_errors=True)
