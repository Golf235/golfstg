import subprocess
import os
import time

log_file = '/Users/sebastianlilliecreutz/Downloads/Home - Golfyr_files/chrome_debug.log'
if os.path.exists(log_file):
    os.remove(log_file)

# Command to run chrome and capture console log output
# We can set --user-data-dir to a temporary directory in the workspace
user_data_dir = '/Users/sebastianlilliecreutz/Downloads/Home - Golfyr_files/chrome_profile'
if not os.path.exists(user_data_dir):
    os.makedirs(user_data_dir)

cmd = [
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "--headless",
    "--disable-gpu",
    f"--user-data-dir={user_data_dir}",
    "--enable-logging",
    "--v=1",
    "file:///Users/sebastianlilliecreutz/Downloads/Home - Golfyr_files/technology.html#material"
]

print("Launching Chrome to collect console logs...")
# Run for 5 seconds to let the scripts execute
try:
    subprocess.run(cmd, timeout=5, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
except subprocess.TimeoutExpired as e:
    # This is expected since Chrome keeps running
    stdout = e.stdout
    stderr = e.stderr
    print("Chrome execution finished (timeout reached).")

# Look for chrome_debug.log in the user data dir
chrome_log = os.path.join(user_data_dir, 'chrome_debug.log')
if os.path.exists(chrome_log):
    with open(chrome_log, 'r', encoding='utf-8', errors='ignore') as f:
        log_content = f.read()
    print("\n--- CHROME LOG CONTENTS ---")
    # Print lines that contain CONSOLE
    for line in log_content.split('\n'):
        if 'CONSOLE' in line or 'Error' in line or 'Failed' in line or 'exception' in line:
            print(line)
else:
    print("Could not find chrome_debug.log in user data dir.")
    # check if there is stderr output
    if stderr:
        print("\n--- STDERR ---")
        print(stderr.decode('utf-8', errors='ignore')[:2000])

# Clean up profile
import shutil
shutil.rmtree(user_data_dir, ignore_errors=True)
