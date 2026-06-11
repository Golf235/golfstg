import re
import json

def validate():
    # Read index.html
    with open('/Users/sebastianlilliecreutz/Downloads/Home - Golfyr_files/index.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # Find all data-translate values in HTML
    keys_in_html = set(re.findall(r'data-translate="([^"]+)"', html))
    print(f"Total unique translation keys in HTML: {len(keys_in_html)}")

    # Read rebuilt-app.js
    with open('/Users/sebastianlilliecreutz/Downloads/Home - Golfyr_files/rebuilt-app.js', 'r', encoding='utf-8') as f:
        js = f.read()

    # Extract english and german translations
    # Find translations object: const translations = { ... };
    # Let's search using regex for en: { ... } and de: { ... }
    en_match = re.search(r'en:\s*\{(.*?)\},\s*de:', js, re.DOTALL)
    de_match = re.search(r'de:\s*\{(.*?)\}\s*\}\s*;', js, re.DOTALL)

    if not en_match or not de_match:
        print("Could not extract translation blocks from rebuilt-app.js!")
        return

    en_block = en_match.group(1)
    de_block = de_match.group(1)

    # Parse keys from block
    def parse_keys(block):
        kv = {}
        for line in block.split('\n'):
            line = line.strip()
            if not line:
                continue
            # match "key": "value"
            m = re.match(r'"([^"]+)":\s*"(.*?)",?$', line)
            if m:
                kv[m.group(1)] = m.group(2)
        return kv

    en_kv = parse_keys(en_block)
    de_kv = parse_keys(de_block)

    print(f"English keys: {len(en_kv)}")
    print(f"German keys: {len(de_kv)}")

    # Check for keys in HTML that are missing in JS
    missing_en = []
    missing_de = []
    for key in sorted(keys_in_html):
        if key not in en_kv:
            missing_en.append(key)
        if key not in de_kv:
            missing_de.append(key)

    if missing_en:
        print(f"\nMissing English keys for HTML data-translates: {missing_en}")
    else:
        print("\nNo missing English keys!")

    if missing_de:
        print(f"Missing German keys for HTML data-translates: {missing_de}")
    else:
        print("No missing German keys!")

    # Check for slides in the map section
    # Let's check info-card data-translates specifically
    map_section_matches = re.findall(r'<div class="info-card-title"\s+data-translate="([^"]+)">.*?</div>\s*<div class="info-card-icon">.*?</div>\s*</div>\s*<p class="info-card-desc"\s+data-translate="([^"]+)">', html, re.DOTALL)
    print(f"\nMap section found {len(map_section_matches)} club detail cards:")
    for title_key, desc_key in map_section_matches:
        print(f"  Title Key: {title_key} ({en_kv.get(title_key, 'MISSING')}) | Desc Key: {desc_key} ({en_kv.get(desc_key, 'MISSING')})")

validate()
