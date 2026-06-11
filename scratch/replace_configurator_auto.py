import os

js_filepath = "/Users/sebastianlilliecreutz/Downloads/Home - Golfyr_files/Golfyr Configurator V2_files/index-CpiWRb-T.js"

if not os.path.exists(js_filepath):
    print("JS file does not exist!")
    exit(1)

with open(js_filepath, "r", encoding="utf-8") as f:
    content = f.read()

# Backup current file
backup_filepath = js_filepath + ".tmp_bak"
with open(backup_filepath, "w", encoding="utf-8") as f:
    f.write(content)
print("Created temporary backup at index-CpiWRb-T.js.tmp_bak")

new_content = content

# Replace bg.map (Model) -> open Shaft ('exterior')
target_bg = 'bg.map(R=>M.jsxs("button",{onClick:()=>C(R)'
replacement_bg = 'bg.map(R=>M.jsxs("button",{onClick:()=>{C(R);S("exterior")}'

# Replace vg.map (Shaft) -> open Grip ('wheels')
target_vg = 'vg.map(R=>M.jsxs("button",{onClick:()=>x(R)'
replacement_vg = 'vg.map(R=>M.jsxs("button",{onClick:()=>{x(R);S("wheels")}'

# Replace xg.map (Grip) -> open Putter ('interior')
target_xg = 'xg.map(R=>M.jsxs("button",{onClick:()=>_(R)'
replacement_xg = 'xg.map(R=>M.jsxs("button",{onClick:()=>{_(R);S("interior")}'

if target_bg in new_content:
    new_content = new_content.replace(target_bg, replacement_bg)
    print("Replaced Model transition")
else:
    print("WARNING: Model transition target not found!")

if target_vg in new_content:
    new_content = new_content.replace(target_vg, replacement_vg)
    print("Replaced Shaft transition")
else:
    print("WARNING: Shaft transition target not found!")

if target_xg in new_content:
    new_content = new_content.replace(target_xg, replacement_xg)
    print("Replaced Grip transition")
else:
    print("WARNING: Grip transition target not found!")

if new_content != content:
    with open(js_filepath, "w", encoding="utf-8") as f:
        f.write(new_content)
    print("Successfully updated index-CpiWRb-T.js")
else:
    print("No changes were made to the file.")
