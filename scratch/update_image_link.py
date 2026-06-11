js_path = "/Users/sebastianlilliecreutz/Downloads/Home - Golfyr_files/Golfyr Configurator V2_files/index-CpiWRb-T.js"

with open(js_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Target string
target = 'ie=[{id:"all",name:"All",image:"./premier_set.png",extraImages:["./premier_set.png","./Golfyr Configurator V2_files/the-premier-set-600x600.jpg"]}'
replacement = 'ie=[{id:"all",name:"All",image:"./Maker Tour - Golfyr_files/2026_Marketint_Set_Images_02.jpg",extraImages:["./Maker Tour - Golfyr_files/2026_Marketint_Set_Images_02.jpg","./Golfyr Configurator V2_files/the-premier-set-600x600.jpg"]}'

if target in content:
    print("Found exact target string!")
    new_content = content.replace(target, replacement)
    with open(js_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Replacement complete!")
else:
    print("Target string NOT found! Checking if there are other occurrences of './premier_set.png'...")
    import re
    matches = re.findall(r'premier_set\.png', content)
    print(f"Occurrences found: {len(matches)}")
