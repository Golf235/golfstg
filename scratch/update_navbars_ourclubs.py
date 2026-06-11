import os
import re

html_dir = '/Users/sebastianlilliecreutz/Downloads/Home - Golfyr_files'

files_to_process = [
    f for f in os.listdir(html_dir) 
    if f.endswith('.html') and f != 'configurator.html' and not f.startswith('saved_resource') and f != 'temp_tablet_fixed_heights.html'
]

print(f"Found {len(files_to_process)} HTML files to update.")

# Desktop pattern and replacement
desktop_pattern = re.compile(
    r'<ul class="dropdown-menu">\s*'
    r'<li><a href="(?:\./)?sevenclubgame\.html"\s*data-translate="nav-sevenclub">#sevenclubgame</a></li>\s*'
    r'<li><hr style="margin: 4px 0; border: 0; border-top: 1px solid rgba\(0,0,0,0\.08\);"></li>\s*'
    r'<li><a href="(?:\./)?opener\.html"\s*data-translate="club-opener-title">The Opener</a></li>\s*'
    r'<li><a href="(?:\./)?mover\.html"\s*data-translate="club-mover-title">The Mover</a></li>\s*'
    r'<li><a href="(?:\./)?riser\.html"\s*data-translate="club-riser-title">The Riser</a></li>\s*'
    r'<li><a href="(?:\./)?pitcher\.html"\s*data-translate="club-pitcher-title">The Pitcher</a></li>\s*'
    r'<li><a href="(?:\./)?maker\.html"\s*data-translate="club-maker-title">The Maker</a></li>\s*'
    r'<li><a href="(?:\./)?saver\.html"\s*data-translate="club-saver-title">The Saver</a></li>\s*'
    r'<li><a href="(?:\./)?butler\.html"\s*data-translate="club-butler-title">The Butler</a></li>\s*'
    r'</ul>',
    re.DOTALL
)

desktop_replacement = '''<ul class="dropdown-menu">
                            <li><a href="./sevenclubgame.html" data-translate="nav-sevenclub" class="dropdown-category">#sevenclubgame</a></li>
                            <li><a href="./opener.html" data-translate="club-opener-title" class="dropdown-sub-item">The Opener</a></li>
                            <li><a href="./mover.html" data-translate="club-mover-title" class="dropdown-sub-item">The Mover</a></li>
                            <li><a href="./riser.html" data-translate="club-riser-title" class="dropdown-sub-item">The Riser</a></li>
                            <li><a href="./pitcher.html" data-translate="club-pitcher-title" class="dropdown-sub-item">The Pitcher</a></li>
                            <li><a href="./maker.html" data-translate="club-maker-title" class="dropdown-sub-item">The Maker</a></li>
                            <li><a href="./saver.html" data-translate="club-saver-title" class="dropdown-sub-item">The Saver</a></li>
                            <li><a href="./butler.html" data-translate="club-butler-title" class="dropdown-sub-item">The Butler</a></li>
                        </ul>'''

# Mobile pattern and replacement
mobile_pattern = re.compile(
    r'<ul class="mobile-sub-menu">\s*'
    r'<li><a href="(?:\./)?sevenclubgame\.html"\s*data-translate="nav-sevenclub"\s*style="font-size: 20px !important;">#sevenclubgame</a></li>\s*'
    r'<li><a href="(?:\./)?opener\.html"\s*data-translate="club-opener-title"\s*style="font-size: 20px !important;">The Opener</a></li>\s*'
    r'<li><a href="(?:\./)?mover\.html"\s*data-translate="club-mover-title"\s*style="font-size: 20px !important;">The Mover</a></li>\s*'
    r'<li><a href="(?:\./)?riser\.html"\s*data-translate="club-riser-title"\s*style="font-size: 20px !important;">The Riser</a></li>\s*'
    r'<li><a href="(?:\./)?pitcher\.html"\s*data-translate="club-pitcher-title"\s*style="font-size: 20px !important;">The Pitcher</a></li>\s*'
    r'<li><a href="(?:\./)?maker\.html"\s*data-translate="club-maker-title"\s*style="font-size: 20px !important;">The Maker</a></li>\s*'
    r'<li><a href="(?:\./)?saver\.html"\s*data-translate="club-saver-title"\s*style="font-size: 20px !important;">The Saver</a></li>\s*'
    r'<li><a href="(?:\./)?butler\.html"\s*data-translate="club-butler-title"\s*style="font-size: 20px !important;">The Butler</a></li>\s*'
    r'</ul>',
    re.DOTALL
)

mobile_replacement = '''<ul class="mobile-sub-menu">
                    <li><a href="./sevenclubgame.html" data-translate="nav-sevenclub" class="dropdown-category">#sevenclubgame</a></li>
                    <li><a href="./opener.html" data-translate="club-opener-title" class="dropdown-sub-item">The Opener</a></li>
                    <li><a href="./mover.html" data-translate="club-mover-title" class="dropdown-sub-item">The Mover</a></li>
                    <li><a href="./riser.html" data-translate="club-riser-title" class="dropdown-sub-item">The Riser</a></li>
                    <li><a href="./pitcher.html" data-translate="club-pitcher-title" class="dropdown-sub-item">The Pitcher</a></li>
                    <li><a href="./maker.html" data-translate="club-maker-title" class="dropdown-sub-item">The Maker</a></li>
                    <li><a href="./saver.html" data-translate="club-saver-title" class="dropdown-sub-item">The Saver</a></li>
                    <li><a href="./butler.html" data-translate="club-butler-title" class="dropdown-sub-item">The Butler</a></li>
                </ul>'''

updated_count = 0

for filename in files_to_process:
    filepath = os.path.join(html_dir, filename)
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    modified = False
    
    # 1. Update Desktop Dropdown
    new_content, d_count = desktop_pattern.subn(desktop_replacement, content)
    if d_count > 0:
        content = new_content
        modified = True
    else:
        # Check if already has class="dropdown-category" or if it didn't match
        if 'class="dropdown-category"' not in content:
            print(f"WARNING: Desktop menu did not match in {filename}")
            
    # 2. Update Mobile Menu
    new_content, m_count = mobile_pattern.subn(mobile_replacement, content)
    if m_count > 0:
        content = new_content
        modified = True
    else:
        if 'class="dropdown-category"' not in content:
            print(f"WARNING: Mobile menu did not match in {filename}")
            
    if modified:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {filename}: desktop={d_count}, mobile={m_count}")
        updated_count += 1
    else:
        print(f"No changes needed / Already updated: {filename}")

print(f"Completed! Total files modified: {updated_count}/{len(files_to_process)}")
