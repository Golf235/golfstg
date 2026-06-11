import re
import os
import glob

def parse_js_translations():
    with open('rebuilt-app.js', 'r', encoding='utf-8') as f:
        js = f.read()

    # Find the translations block and parse keys
    # Let's search using regex for en: { ... } and de: { ... }
    en_match = re.search(r'en:\s*\{(.*?)\},\s*de:', js, re.DOTALL)
    de_match = re.search(r'de:\s*\{(.*?)\}\s*\}\s*;', js, re.DOTALL)

    if not en_match or not de_match:
        raise ValueError("Could not extract translation blocks from rebuilt-app.js!")

    en_block = en_match.group(1)
    de_block = de_match.group(1)

    def parse_keys(block):
        kv = {}
        # Simple extraction of key/value pairs using regex
        matches = re.findall(r'"([^"]+)":\s*(?:"([^"]+)"|`([^`]+)`|span|div|em|bdi)', block)
        # We can also search line by line for precision
        for line in block.split('\n'):
            line = line.strip()
            if not line:
                continue
            m = re.match(r'"([^"]+)":\s*"(.*?)",?$', line)
            if m:
                kv[m.group(1)] = m.group(2)
            else:
                # Fallback for complex lines containing single quotes/HTML
                m2 = re.match(r'"([^"]+)":\s*(?:`|")(.*?)(?:`|"),?$', line)
                if m2:
                    kv[m2.group(1)] = m2.group(2)
        return kv

    return parse_keys(en_block), parse_keys(de_block)

def main():
    print("=== SEVENCLUBGAME OVERVIEW PAGE VERIFICATION ===")
    
    # 1. Read sevenclubgame.html
    if not os.path.exists('sevenclubgame.html'):
        print("ERROR: sevenclubgame.html does not exist!")
        return
        
    with open('sevenclubgame.html', 'r', encoding='utf-8') as f:
        html = f.read()
        
    # Extract data-translate keys
    translate_keys = set(re.findall(r'data-translate="([^"]+)"', html))
    # Extract data-translate-src keys
    src_keys = set(re.findall(r'data-translate-src="([^"]+)"', html))
    # Extract data-translate-srcset keys
    srcset_keys = set(re.findall(r'data-translate-srcset="([^"]+)"', html))
    
    all_html_keys = translate_keys.union(src_keys).union(srcset_keys)
    print(f"Found {len(all_html_keys)} total translation/src keys in sevenclubgame.html:")
    print(f"  - data-translate keys: {len(translate_keys)}")
    print(f"  - data-translate-src keys: {len(src_keys)}")
    print(f"  - data-translate-srcset keys: {len(srcset_keys)}")
    
    # 2. Get keys from JS
    en_kv, de_kv = parse_js_translations()
    
    # Check alignment
    missing_en = []
    missing_de = []
    for key in sorted(all_html_keys):
        # We can bypass global nav keys if they are checked elsewhere, but checking them is fine
        if key not in en_kv:
            missing_en.append(key)
        if key not in de_kv:
            missing_de.append(key)
            
    if missing_en:
        print(f"\n[FAIL] Missing English keys in rebuilt-app.js: {missing_en}")
    else:
        print("\n[PASS] All keys present in rebuilt-app.js (English)!")
        
    if missing_de:
        print(f"[FAIL] Missing German keys in rebuilt-app.js: {missing_de}")
    else:
        print("[PASS] All keys present in rebuilt-app.js (German)!")
        
    # 3. Check legacy link occurrences in headers/footers/drawers
    print("\nChecking for legacy #sevenclubgame links in navigation menus, drawers, and footers...")
    legacy_patterns = [
        r'href="#sevenclubgame"',
        r'href="./index.html#sevenclubgame"'
    ]
    
    issues_found = False
    html_files = glob.glob('*.html')
    for filepath in sorted(html_files):
        with open(filepath, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            
        for idx, line in enumerate(lines):
            # Check if href contains #sevenclubgame or ./index.html#sevenclubgame
            m = re.search(r'href="([^"]*#sevenclubgame)"', line)
            if m and ('<li>' in line or 'footer' in filepath or idx > len(lines) - 200 or idx < 100):
                # We expect sevenclubgame.html itself to point to its sections using # if needed, but not legacy ones
                if filepath == 'sevenclubgame.html':
                    continue
                print(f"  [FAIL] Legacy link at {filepath}:{idx+1}: {line.strip()}")
                issues_found = True
                
    if not issues_found:
        print("[PASS] No legacy links found in headers, mobile drawers, or footers across all HTML pages!")
    else:
        print("[FAIL] Some legacy links were found!")
        
if __name__ == '__main__':
    main()
