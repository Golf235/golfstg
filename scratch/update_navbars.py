import os
import re

html_dir = '/Users/sebastianlilliecreutz/Downloads/Home - Golfyr_files'

files_to_process = [
    f for f in os.listdir(html_dir) 
    if f.endswith('.html') and f != 'configurator.html' and not f.startswith('saved_resource')
]

print(f"Found {len(files_to_process)} HTML files to update.")

for filename in files_to_process:
    filepath = os.path.join(html_dir, filename)
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    modified = False
    
    # 1. Match desktop nav links
    nav_links_match = re.search(r'(<ul class="nav-links">.*?</ul>)', content, re.DOTALL)
    if nav_links_match:
        nav_links_block = nav_links_match.group(1)
        # Check if already updated
        if 'class="nav-dropdown"' not in nav_links_block:
            new_nav_links_block = re.sub(
                r'<li><a href="(?:\./)?sevenclubgame\.html"([^>]*)>#sevenclubgame</a></li>',
                lambda m: f'''<li class="nav-dropdown">
                        <a href="./sevenclubgame.html"{m.group(1)}>#sevenclubgame <svg class="arrow-icon" width="10" height="6" viewBox="0 0 10 6" fill="none" xmlns="http://www.w3.org/2000/svg" style="margin-left: 6px; transition: transform var(--transition-smooth);"><path d="M1 1L5 5L9 1" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg></a>
                        <ul class="dropdown-menu">
                            <li><a href="./opener.html" data-translate="club-opener-title">The Opener</a></li>
                            <li><a href="./mover.html" data-translate="club-mover-title">The Mover</a></li>
                            <li><a href="./riser.html" data-translate="club-riser-title">The Riser</a></li>
                            <li><a href="./pitcher.html" data-translate="club-pitcher-title">The Pitcher</a></li>
                            <li><a href="./maker.html" data-translate="club-maker-title">The Maker</a></li>
                            <li><a href="./saver.html" data-translate="club-saver-title">The Saver</a></li>
                            <li><a href="./butler.html" data-translate="club-butler-title">The Butler</a></li>
                        </ul>
                    </li>''',
                nav_links_block
            )
            content = content.replace(nav_links_block, new_nav_links_block)
            modified = True
            
    # 2. Match mobile menu links
    mobile_links_match = re.search(r'(<ul class="mobile-menu-links">.*?</ul>)', content, re.DOTALL)
    if mobile_links_match:
        mobile_links_block = mobile_links_match.group(1)
        # Check if already updated
        if 'class="mobile-nav-dropdown"' not in mobile_links_block:
            new_mobile_links_block = re.sub(
                r'<li><a href="(?:\./)?sevenclubgame\.html"([^>]*)>#sevenclubgame</a></li>',
                lambda m: f'''<li class="mobile-nav-dropdown">
                <a href="javascript:void(0)" class="mobile-dropdown-trigger">#sevenclubgame <svg class="arrow-icon" width="12" height="8" viewBox="0 0 12 8" fill="none" xmlns="http://www.w3.org/2000/svg" style="margin-left: 8px; transition: transform var(--transition-smooth);"><path d="M1 1.5L6 6.5L11 1.5" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg></a>
                <ul class="mobile-sub-menu">
                    <li><a href="./sevenclubgame.html" data-translate="nav-sevenclub-all" style="font-size: 20px !important;">All Clubs</a></li>
                    <li><a href="./opener.html" data-translate="club-opener-title" style="font-size: 20px !important;">The Opener</a></li>
                    <li><a href="./mover.html" data-translate="club-mover-title" style="font-size: 20px !important;">The Mover</a></li>
                    <li><a href="./riser.html" data-translate="club-riser-title" style="font-size: 20px !important;">The Riser</a></li>
                    <li><a href="./pitcher.html" data-translate="club-pitcher-title" style="font-size: 20px !important;">The Pitcher</a></li>
                    <li><a href="./maker.html" data-translate="club-maker-title" style="font-size: 20px !important;">The Maker</a></li>
                    <li><a href="./saver.html" data-translate="club-saver-title" style="font-size: 20px !important;">The Saver</a></li>
                    <li><a href="./butler.html" data-translate="club-butler-title" style="font-size: 20px !important;">The Butler</a></li>
                </ul>
            </li>''',
                mobile_links_block
            )
            content = content.replace(mobile_links_block, new_mobile_links_block)
            modified = True

    # 3. Remove Maker Tour links
    new_content, count = re.subn(r'<li><a href="(?:\./)?maker-tour\.html"[^>]*>Maker Tour</a></li>', '', content)
    if count > 0:
        content = new_content
        modified = True
        
    if modified:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated: {filename} (Removed {count} Maker Tour links)")

print("Completed successfully!")
