import os
import glob

workspace_dir = '/Users/sebastianlilliecreutz/Downloads/Home - Golfyr_files'
html_files = glob.glob(os.path.join(workspace_dir, '*.html'))

# 1. Targets for #sevenclubgame desktop link
sevenclub_target_normal = '<a href="./sevenclubgame.html" data-translate="nav-sevenclub">#sevenclubgame <svg class="arrow-icon" width="10" height="6" viewBox="0 0 10 6" fill="none" xmlns="http://www.w3.org/2000/svg" style="margin-left: 6px; transition: transform var(--transition-smooth);"><path d="M1 1L5 5L9 1" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg></a>'
sevenclub_target_active = '<a href="./sevenclubgame.html" class="active" data-translate="nav-sevenclub">#sevenclubgame <svg class="arrow-icon" width="10" height="6" viewBox="0 0 10 6" fill="none" xmlns="http://www.w3.org/2000/svg" style="margin-left: 6px; transition: transform var(--transition-smooth);"><path d="M1 1L5 5L9 1" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg></a>'

sevenclub_replacement_normal = '<a href="./sevenclubgame.html"><span data-translate="nav-sevenclub">#sevenclubgame</span> <svg class="arrow-icon" width="10" height="6" viewBox="0 0 10 6" fill="none" xmlns="http://www.w3.org/2000/svg" style="margin-left: 6px; transition: transform var(--transition-smooth);"><path d="M1 1L5 5L9 1" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg></a>'
sevenclub_replacement_active = '<a href="./sevenclubgame.html" class="active"><span data-translate="nav-sevenclub">#sevenclubgame</span> <svg class="arrow-icon" width="10" height="6" viewBox="0 0 10 6" fill="none" xmlns="http://www.w3.org/2000/svg" style="margin-left: 6px; transition: transform var(--transition-smooth);"><path d="M1 1L5 5L9 1" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg></a>'

# 2. Dropdown replacements for Technology desktop link
# The previous script already replaced the old single link with a dropdown structure.
# So we need to look for that replaced structure or target it. Let's list the two versions we generated in the first run.
old_desktop_rep_normal = """                    <li class="nav-dropdown">
                        <a href="./technology.html" data-translate="nav-tech">Technology <svg class="arrow-icon" width="10" height="6" viewBox="0 0 10 6" fill="none" xmlns="http://www.w3.org/2000/svg" style="margin-left: 6px; transition: transform var(--transition-smooth);"><path d="M1 1L5 5L9 1" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg></a>
                        <ul class="dropdown-menu">
                            <li><a href="./innovation.html" data-translate="nav-innovation">Innovation</a></li>
                            <li><a href="./material.html" data-translate="nav-material">Material</a></li>
                            <li><a href="./production.html" data-translate="nav-production">Production</a></li>
                        </ul>
                    </li>"""

old_desktop_rep_active = """                    <li class="nav-dropdown">
                        <a href="./technology.html" class="active" data-translate="nav-tech">Technology <svg class="arrow-icon" width="10" height="6" viewBox="0 0 10 6" fill="none" xmlns="http://www.w3.org/2000/svg" style="margin-left: 6px; transition: transform var(--transition-smooth);"><path d="M1 1L5 5L9 1" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg></a>
                        <ul class="dropdown-menu">
                            <li><a href="./innovation.html" data-translate="nav-innovation">Innovation</a></li>
                            <li><a href="./material.html" data-translate="nav-material">Material</a></li>
                            <li><a href="./production.html" data-translate="nav-production">Production</a></li>
                        </ul>
                    </li>"""

# We replace them with the chevron-safe span version:
new_desktop_rep_normal = """                    <li class="nav-dropdown">
                        <a href="./technology.html"><span data-translate="nav-tech">Technology</span> <svg class="arrow-icon" width="10" height="6" viewBox="0 0 10 6" fill="none" xmlns="http://www.w3.org/2000/svg" style="margin-left: 6px; transition: transform var(--transition-smooth);"><path d="M1 1L5 5L9 1" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg></a>
                        <ul class="dropdown-menu">
                            <li><a href="./innovation.html" data-translate="nav-innovation">Innovation</a></li>
                            <li><a href="./material.html" data-translate="nav-material">Material</a></li>
                            <li><a href="./production.html" data-translate="nav-production">Production</a></li>
                        </ul>
                    </li>"""

new_desktop_rep_active = """                    <li class="nav-dropdown">
                        <a href="./technology.html" class="active"><span data-translate="nav-tech">Technology</span> <svg class="arrow-icon" width="10" height="6" viewBox="0 0 10 6" fill="none" xmlns="http://www.w3.org/2000/svg" style="margin-left: 6px; transition: transform var(--transition-smooth);"><path d="M1 1L5 5L9 1" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg></a>
                        <ul class="dropdown-menu">
                            <li><a href="./innovation.html" data-translate="nav-innovation">Innovation</a></li>
                            <li><a href="./material.html" data-translate="nav-material">Material</a></li>
                            <li><a href="./production.html" data-translate="nav-production">Production</a></li>
                        </ul>
                    </li>"""

# 3. Mobile replacement
old_mobile_rep = """            <li class="mobile-nav-dropdown">
                <a href="javascript:void(0)" class="mobile-dropdown-trigger" data-translate="nav-tech">Technology <svg class="arrow-icon" width="12" height="8" viewBox="0 0 12 8" fill="none" xmlns="http://www.w3.org/2000/svg" style="margin-left: 8px; transition: transform var(--transition-smooth);"><path d="M1 1.5L6 6.5L11 1.5" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg></a>
                <ul class="mobile-sub-menu">
                    <li><a href="./technology.html" data-translate="nav-tech-all" style="font-size: 20px !important;">All Technology</a></li>
                    <li><a href="./innovation.html" data-translate="nav-innovation" style="font-size: 20px !important;">Innovation</a></li>
                    <li><a href="./material.html" data-translate="nav-material" style="font-size: 20px !important;">Material</a></li>
                    <li><a href="./production.html" data-translate="nav-production" style="font-size: 20px !important;">Production</a></li>
                </ul>
            </li>"""

new_mobile_rep = """            <li class="mobile-nav-dropdown">
                <a href="javascript:void(0)" class="mobile-dropdown-trigger"><span data-translate="nav-tech">Technology</span> <svg class="arrow-icon" width="12" height="8" viewBox="0 0 12 8" fill="none" xmlns="http://www.w3.org/2000/svg" style="margin-left: 8px; transition: transform var(--transition-smooth);"><path d="M1 1.5L6 6.5L11 1.5" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg></a>
                <ul class="mobile-sub-menu">
                    <li><a href="./technology.html" data-translate="nav-tech-all" style="font-size: 20px !important;">All Technology</a></li>
                    <li><a href="./innovation.html" data-translate="nav-innovation" style="font-size: 20px !important;">Innovation</a></li>
                    <li><a href="./material.html" data-translate="nav-material" style="font-size: 20px !important;">Material</a></li>
                    <li><a href="./production.html" data-translate="nav-production" style="font-size: 20px !important;">Production</a></li>
                </ul>
            </li>"""

tech_pages = ['technology.html', 'innovation.html', 'material.html', 'production.html']

updated_count = 0

for filepath in html_files:
    basename = os.path.basename(filepath)
    if basename.startswith('temp_verify_') or basename.startswith('temp_formats_'):
        continue
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    original = content
    
    # 1. Update Sevenclubgame desktop links
    if sevenclub_target_normal in content:
        content = content.replace(sevenclub_target_normal, sevenclub_replacement_normal)
    if sevenclub_target_active in content:
        content = content.replace(sevenclub_target_active, sevenclub_replacement_active)
        
    # 2. Update Technology desktop links
    if old_desktop_rep_normal in content:
        content = content.replace(old_desktop_rep_normal, new_desktop_rep_normal)
    if old_desktop_rep_active in content:
        content = content.replace(old_desktop_rep_active, new_desktop_rep_active)
        
    # 3. Update Technology mobile links
    if old_mobile_rep in content:
        content = content.replace(old_mobile_rep, new_mobile_rep)
        
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {basename}")
        updated_count += 1
    else:
        print(f"No changes in {basename}")

print(f"Finished. Updated {updated_count} files.")
