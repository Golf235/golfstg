import subprocess
import os
import urllib.parse

# Read the configurator.html content
configurator_path = "/Users/sebastianlilliecreutz/Downloads/Home - Golfyr_files/configurator.html"
with open(configurator_path, "r", encoding="utf-8") as f:
    content = f.read()

# Script to inject to automatically open Shaft on load
inject_script = """
<script>
window.addEventListener('load', () => {
    setTimeout(() => {
        // Find buttons containing accordion text
        const buttons = Array.from(document.querySelectorAll('button'));
        const gripBtn = buttons.find(btn => btn.textContent.trim().startsWith('Grip'));
        if (gripBtn) {
            console.log("Found Grip button, clicking...");
            gripBtn.click();
        } else {
            console.log("Grip button not found");
        }
    }, 500);
});
</script>
"""

# Inject script before the closing </body> tag
test_content = content.replace("</body>", inject_script + "\n</body>")
temp_file = "/Users/sebastianlilliecreutz/Downloads/Home - Golfyr_files/temp_test_options.html"
with open(temp_file, "w", encoding="utf-8") as f:
    f.write(test_content)

# Take screenshots at different widths
chrome_path = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

sizes = [
    ("desktop", 1440, 2500),
    ("tablet", 768, 2500),
    ("mobile", 375, 2500)
]

for name, width, height in sizes:
    out_path = f"/Users/sebastianlilliecreutz/.gemini/antigravity/brain/b15a35fe-c2ee-485e-bc8c-5ee93ec01292/configurator_{name}_grip_open.png"
    cmd = [
        chrome_path,
        "--headless",
        "--disable-gpu",
        f"--screenshot={out_path}",
        f"--window-size={width},{height}",
        "--virtual-time-budget=3000",
        f"file://{temp_file}"
    ]
    print(f"Running headless Chrome for Grip section ({name})...")
    subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

# Clean up temp file
if os.path.exists(temp_file):
    os.remove(temp_file)

print("Finished! Screenshots saved.")
