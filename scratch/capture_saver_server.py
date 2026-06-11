import subprocess
import os
import time
import http.server
import socketserver
import threading

PORT = 8089
DIRECTORY = "/Users/sebastianlilliecreutz/Downloads/Home - Golfyr_files"
artifact_dir = "/Users/sebastianlilliecreutz/.gemini/antigravity/brain/b15a35fe-c2ee-485e-bc8c-5ee93ec01292"

# A simple custom HTTP handler to serve files from the directory
class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

def start_server():
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"Serving HTTP on port {PORT}...")
        httpd.serve_forever()

# Start HTTP server in a background thread
server_thread = threading.Thread(target=start_server, daemon=True)
server_thread.start()

# Give the server a moment to start
time.sleep(1)

# List of screenshots to capture
captures = [
    {
        "name": "saver_desktop_hero.png",
        "url": f"http://localhost:{PORT}/saver.html",
        "size": "1200,900"
    },
    {
        "name": "saver_desktop_why.png",
        "url": f"http://localhost:{PORT}/saver.html#why-pitcher",
        "size": "1200,900"
    },
    {
        "name": "saver_desktop_specs.png",
        "url": f"http://localhost:{PORT}/saver.html#tech-specs",
        "size": "1200,900"
    },
    {
        "name": "saver_mobile_hero.png",
        "url": f"http://localhost:{PORT}/saver.html",
        "size": "390,844"
    },
    {
        "name": "saver_mobile_why.png",
        "url": f"http://localhost:{PORT}/saver.html#why-pitcher",
        "size": "390,844"
    }
]

for cap in captures:
    out_img = os.path.join(artifact_dir, cap["name"])
    cmd = [
        "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
        "--headless",
        "--disable-gpu",
        f"--screenshot={out_img}",
        f"--window-size={cap['size']}",
        "--virtual-time-budget=3000",
        cap["url"]
    ]
    print(f"Capturing {cap['name']} from {cap['url']}...")
    subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    
    if os.path.exists(out_img):
        print(f"Successfully captured {cap['name']} ({os.path.getsize(out_img)} bytes)")
    else:
        print(f"Failed to capture {cap['name']}")

print("All captures complete.")
