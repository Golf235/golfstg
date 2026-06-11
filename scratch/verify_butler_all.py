import re
import sys
import os

def check_translations():
    print("--- Checking Translation Keys Alignment ---")
    with open('butler.html', 'r', encoding='utf-8') as f:
        html = f.read()

    keys_in_html = set(re.findall(r'data-translate="([^"]+)"', html))
    print(f"Total unique translation keys in butler.html: {len(keys_in_html)}")

    with open('rebuilt-app.js', 'r', encoding='utf-8') as f:
        js = f.read()

    en_match = re.search(r'en:\s*\{(.*?)\},\s*de:', js, re.DOTALL)
    de_match = re.search(r'de:\s*\{(.*?)\}\s*\}\s*;', js, re.DOTALL)

    if not en_match or not de_match:
        print("Error: Could not extract translation blocks from rebuilt-app.js!")
        return False

    en_block = en_match.group(1)
    de_block = de_match.group(1)

    def parse_keys(block):
        kv = {}
        for line in block.split('\n'):
            line = line.strip()
            if not line:
                continue
            m = re.match(r'"([^"]+)":\s*"(.*?)",?$', line)
            if m:
                kv[m.group(1)] = m.group(2)
        return kv

    en_kv = parse_keys(en_block)
    de_kv = parse_keys(de_block)

    missing_en = []
    missing_de = []
    for key in sorted(keys_in_html):
        if key not in en_kv:
            missing_en.append(key)
        if key not in de_kv:
            missing_de.append(key)

    if missing_en:
        print(f"Missing English keys: {missing_en}")
    else:
        print("No missing English keys!")

    if missing_de:
        print(f"Missing German keys: {missing_de}")
    else:
        print("No missing German keys!")

    if missing_en or missing_de:
        return False
    
    print("Translation validation PASSED!")
    return True

def check_structure():
    print("\n--- Checking Page Structure and Constraints ---")
    with open('butler.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # Check tab counts (Why section)
    # The tabs list is in `<div class="swiper simpleSliderTabNav">`
    why_tabs = re.findall(r'<div class="menu-tab"[^>]*>.*?</div>', html, re.DOTALL)
    why_slides_img = re.findall(r'<div class="swiper-slide">\s*<div class="image-wrapper">\s*<img src="\./The Butler - Golfyr_files/[^"]+"', html, re.DOTALL)
    why_slides_desc = re.findall(r'<div class="swiper-slide">\s*<div class="content-wrapper">', html, re.DOTALL)

    print(f"Why Tabs found: {len(why_tabs)}")
    print(f"Why Images found: {len(why_slides_img)}")
    print(f"Why Descriptions found: {len(why_slides_desc)}")

    # Check specs counts
    # The specs are in `<div class="swiper swiper-club-tech-specs-slider">`
    spec_slides = re.findall(r'<div class="swiper-slide spec-slide">', html)
    print(f"Tech Specs Slides found: {len(spec_slides)}")

    if len(why_tabs) != 3 or len(why_slides_img) != 3 or len(why_slides_desc) != 3:
        print("Error: Why choose tabs/slides count is not exactly 3!")
        return False
    
    if len(spec_slides) != 4:
        print("Error: Tech specs slides count is not exactly 4!")
        return False

    print("Structure validation PASSED!")
    return True

def check_links():
    print("\n--- Checking Site-wide Links ---")
    all_html_files = [f for f in os.listdir('.') if f.endswith('.html')]
    failures = False
    for filepath in all_html_files:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check for #butler links in footer, our clubs, etc.
        butler_links = re.findall(r'href=["\']\./index\.html#butler["\']|href=["\']#butler["\']', content)
        if butler_links:
            print(f"Error: Found lingering butler section links in {filepath}: {butler_links}")
            failures = True
            
    if not failures:
        print("Link validation PASSED!")
        return True
    return False

if __name__ == '__main__':
    ok_trans = check_translations()
    ok_struct = check_structure()
    ok_links = check_links()
    
    if ok_trans and ok_struct and ok_links:
        print("\nAll checks PASSED successfully!")
        sys.exit(0)
    else:
        print("\nVerification FAILED!")
        sys.exit(1)
