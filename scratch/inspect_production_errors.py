import subprocess
import os
import shutil

user_data_dir = '/Users/sebastianlilliecreutz/Downloads/Home - Golfyr_files/chrome_profile_production_check'
if not os.path.exists(user_data_dir):
    os.makedirs(user_data_dir)

log_file = os.path.join(user_data_dir, 'chrome_debug.log')
if os.path.exists(log_file):
    os.remove(log_file)

cmd = [
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "--headless",
    "--disable-gpu",
    f"--user-data-dir={user_data_dir}",
    "--enable-logging",
    "--v=1",
    "http://localhost:8000/production.html"
]

print("Launching Chrome...")
try:
    subprocess.run(cmd, timeout=5, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
except subprocess.TimeoutExpired:
    print("Chrome execution timeout reached.")

if os.path.exists(log_file):
    with open(log_file, 'r', encoding='utf-8', errors='ignore') as f:
        log_content = f.read()
    print("\n--- CHROME LOG CONTENTS ---")
    for line in log_content.split('\n'):
        if 'CONSOLE' in line or 'error' in line.lower() or 'failed' in line.lower() or 'exception' in line.lower():
            print(line)
else:
    print("Could not find chrome_debug.log.")

shutil.rmtree(user_data_dir, ignore_errors=True)
