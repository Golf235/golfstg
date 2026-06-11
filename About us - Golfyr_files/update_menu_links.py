import os

workspace_dir = '/Users/sebastianlilliecreutz/Downloads/Home - Golfyr_files'

pages = [
    'index.html',
    'magazine.html',
    'innovation.html',
    'material.html',
    'production.html',
    'experience.html'
]

for page in pages:
    filepath = os.path.join(workspace_dir, page)
    if not os.path.exists(filepath):
        print(f"Skipping {page} (does not exist)")
        continue
    
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # Replace navigation links
    # For index.html, replace href="#about" with href="./about.html"
    # For other pages, replace href="./index.html#about" with href="./about.html"
    if page == 'index.html':
        updated_html = html.replace('href="#about"', 'href="./about.html"')
        # Wait, also replace any other menu references if necessary
    else:
        updated_html = html.replace('href="./index.html#about"', 'href="./about.html"')
        
    if updated_html != html:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(updated_html)
        print(f"Updated navigation links in {page}")
    else:
        print(f"No changes in navigation links for {page}")
