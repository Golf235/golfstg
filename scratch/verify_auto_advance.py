import subprocess
import os

configurator_path = "/Users/sebastianlilliecreutz/Downloads/Home - Golfyr_files/configurator.html"
with open(configurator_path, "r", encoding="utf-8") as f:
    content = f.read()

# Injected script to simulate clicks and verify auto-advance
inject_script = """
<script>
window.addEventListener('load', () => {
    const urlParams = new URLSearchParams(window.location.search);
    const step = parseInt(urlParams.get('step') || '0');
    console.log("Starting test for step " + step);
    
    setTimeout(() => {
        // Find and click Model button to open it
        const buttons = Array.from(document.querySelectorAll('button'));
        const modelBtn = buttons.find(btn => btn.textContent.trim().startsWith('Model'));
        if (modelBtn) {
            console.log("Opening Model accordion...");
            modelBtn.click();
        }
        
        setTimeout(() => {
            if (step >= 1) {
                // Find and click first model option
                const modelOptions = Array.from(document.querySelectorAll('button')).filter(btn => 
                    btn.textContent.includes("Standard (Best fit") || 
                    btn.textContent.includes("Standard Light") || 
                    btn.textContent.includes("Light short")
                );
                if (modelOptions.length > 0) {
                    console.log("Clicking model option: " + modelOptions[0].textContent.trim());
                    modelOptions[0].click(); // Standard
                }
            }
            
            setTimeout(() => {
                if (step >= 2) {
                    // Find and click first shaft option
                    const shaftOptions = Array.from(document.querySelectorAll('button')).filter(btn => 
                        btn.textContent.trim() === "Stiff" || 
                        btn.textContent.trim() === "Regular" || 
                        btn.textContent.trim() === "Light"
                    );
                    if (shaftOptions.length > 0) {
                        console.log("Clicking shaft option: " + shaftOptions[0].textContent.trim());
                        shaftOptions[0].click(); // Stiff
                    }
                }
                
                setTimeout(() => {
                    if (step >= 3) {
                        // Find and click first grip option (specifically "Midsize" to avoid ambiguity)
                        const gripOptions = Array.from(document.querySelectorAll('button')).filter(btn => 
                            btn.textContent.trim() === "Standard" || 
                            btn.textContent.trim() === "Midsize" || 
                            btn.textContent.trim() === "Undersize"
                        );
                        const midsizeOpt = gripOptions.find(o => o.textContent.trim() === "Midsize");
                        if (midsizeOpt) {
                            console.log("Clicking grip option: Midsize");
                            midsizeOpt.click();
                        } else if (gripOptions.length > 0) {
                            console.log("Clicking first grip option: " + gripOptions[0].textContent.trim());
                            gripOptions[0].click();
                        }
                    }
                }, 300);
            }, 300);
        }, 300);
    }, 500);
});
</script>
"""

# Inject script before the closing </body> tag
test_content = content.replace("</body>", inject_script + "\n</body>")
temp_file = "/Users/sebastianlilliecreutz/Downloads/Home - Golfyr_files/temp_test_auto_advance.html"
with open(temp_file, "w", encoding="utf-8") as f:
    f.write(test_content)

chrome_path = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

steps = [
    ("step0_initial", 0),
    ("step1_model_selected", 1),
    ("step2_shaft_selected", 2),
    ("step3_grip_selected", 3)
]

for name, step_num in steps:
    out_path = f"/Users/sebastianlilliecreutz/.gemini/antigravity/brain/b15a35fe-c2ee-485e-bc8c-5ee93ec01292/auto_{name}.png"
    url = f"file://{temp_file}?step={step_num}"
    cmd = [
        chrome_path,
        "--headless",
        "--disable-gpu",
        f"--screenshot={out_path}",
        "--window-size=1440,2500",
        "--virtual-time-budget=3000",
        url
    ]
    print(f"Running headless Chrome for {name}...")
    subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

if os.path.exists(temp_file):
    os.remove(temp_file)

print("Screenshots captured successfully!")
