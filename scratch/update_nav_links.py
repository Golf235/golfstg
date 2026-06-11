import os

html_dir = '/Users/sebastianlilliecreutz/Downloads/Home - Golfyr_files'

files_to_process = [
    f for f in os.listdir(html_dir) 
    if f.endswith('.html') and f != 'configurator.html' and not f.startswith('saved_resource') and f != 'temp_tablet_fixed_heights.html'
]

print(f"Found {len(files_to_process)} HTML files to update.")

desktop_find = '''                            <li><a href="./maker.html" data-translate="club-maker-title" class="dropdown-sub-item">The Maker</a></li>
                            <li><a href="./saver.html" data-translate="club-saver-title" class="dropdown-sub-item">The Saver</a></li>'''

desktop_replace = '''                            <li><a href="./maker.html" data-translate="club-maker-title" class="dropdown-sub-item">The Maker</a></li>
                            <li><a href="./maker-tour.html" data-translate="club-makertour-title" class="dropdown-sub-item">The Maker Tour</a></li>
                            <li><a href="./saver.html" data-translate="club-saver-title" class="dropdown-sub-item">The Saver</a></li>'''

mobile_find = '''                    <li><a href="./maker.html" data-translate="club-maker-title" class="dropdown-sub-item">The Maker</a></li>
                    <li><a href="./saver.html" data-translate="club-saver-title" class="dropdown-sub-item">The Saver</a></li>'''

mobile_replace = '''                    <li><a href="./maker.html" data-translate="club-maker-title" class="dropdown-sub-item">The Maker</a></li>
                    <li><a href="./maker-tour.html" data-translate="club-makertour-title" class="dropdown-sub-item">The Maker Tour</a></li>
                    <li><a href="./saver.html" data-translate="club-saver-title" class="dropdown-sub-item">The Saver</a></li>'''

updated_count = 0

for filename in files_to_process:
    filepath = os.path.join(html_dir, filename)
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
        
    original = content
    
    # Replace in desktop menu
    content = content.replace(desktop_find, desktop_replace)
    
    # Replace in mobile menu
    content = content.replace(mobile_find, mobile_replace)
    
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated HTML file: {filename}")
        updated_count += 1
    else:
        print(f"No changes in {filename}")
        
print(f"Finished. Updated {updated_count}/{len(files_to_process)} files.")
