import subprocess
import os
import time
import shutil

user_data_dir = '/Users/sebastianlilliecreutz/Downloads/Home - Golfyr_files/chrome_profile_seven'
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
    "file:///Users/sebastianlilliecreutz/Downloads/Home - Golfyr_files/sevenclubgame.html"
]

print("Launching Chrome to collect console logs for sevenclubgame.html...")
stderr = None
try:
    subprocess.run(cmd, timeout=5, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
except subprocess.TimeoutExpired as e:
    stdout = e.stdout
    stderr = e.stderr
    print("Chrome execution finished (timeout reached).")

if os.path.exists(log_file):
    with open(log_file, 'r', encoding='utf-8', errors='ignore') as f:
        log_content = f.read()
    print("\n--- CHROME LOG CONTENTS ---")
    for line in log_content.split('\n'):
        if 'CONSOLE' in line or 'Error' in line or 'Failed' in line or 'exception' in line:
            print(line)
else:
    print("Could not find chrome_debug.log.")
    if stderr:
        print("\n--- STDERR ---")
        print(stderr.decode('utf-8', errors='ignore')[:2000])

shutil.rmtree(user_data_dir, ignore_errors=True)
