import subprocess
import os

# Read the configurator.html content
configurator_path = "/Users/sebastianlilliecreutz/Downloads/Home - Golfyr_files/configurator.html"
with open(configurator_path, "r", encoding="utf-8") as f:
    content = f.read()

# Script to inject to automatically open Putter on load
inject_script = """
<script>
window.addEventListener('load', () => {
    setTimeout(() => {
        // Find buttons containing accordion text
        const buttons = Array.from(document.querySelectorAll('button'));
        const putterBtn = buttons.find(btn => btn.textContent.trim().startsWith('Putter'));
        if (putterBtn) {
            console.log("Found Putter button, clicking...");
            putterBtn.click();
        } else {
            console.log("Putter button not found");
        }
    }, 500);
});
</script>
"""

# Inject script before the closing </body> tag
test_content = content.replace("</body>", inject_script + "\n</body>")
temp_file = "/Users/sebastianlilliecreutz/Downloads/Home - Golfyr_files/temp_test_putters.html"
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
    out_path = f"/Users/sebastianlilliecreutz/.gemini/antigravity/brain/b15a35fe-c2ee-485e-bc8c-5ee93ec01292/configurator_{name}_putter_open.png"
    cmd = [
        chrome_path,
        "--headless",
        "--disable-gpu",
        f"--screenshot={out_path}",
        f"--window-size={width},{height}",
        "--virtual-time-budget=3000",
        f"file://{temp_file}"
    ]
    print(f"Running headless Chrome for Putter section ({name})...")
    subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

# Clean up temp file
if os.path.exists(temp_file):
    os.remove(temp_file)

print("Finished! Putters screenshots saved.")
