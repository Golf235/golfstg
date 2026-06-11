import re
import sys

def validate():
    # Read pitcher.html
    with open('/Users/sebastianlilliecreutz/Downloads/Home - Golfyr_files/pitcher.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # Find all data-translate values in html
    keys_in_html = set(re.findall(r'data-translate="([^"]+)"', html))
    print(f"Total unique translation keys in pitcher.html: {len(keys_in_html)}")

    # Read rebuilt-app.js
    with open('/Users/sebastianlilliecreutz/Downloads/Home - Golfyr_files/rebuilt-app.js', 'r', encoding='utf-8') as f:
        js = f.read()

    # Extract english and german translations
    # Find translations object: en: { ... } and de: { ... }
    en_match = re.search(r'en:\s*\{(.*?)\},\s*de:', js, re.DOTALL)
    de_match = re.search(r'de:\s*\{(.*?)\}\s*\}\s*;', js, re.DOTALL)

    if not en_match or not de_match:
        print("Could not extract translation blocks from rebuilt-app.js!")
        sys.exit(1)

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

    # Check for keys in HTML that are missing in JS
    missing_en = []
    missing_de = []
    for key in sorted(keys_in_html):
        # Skip shared/generic keys if they are defined in JS
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
        sys.exit(1)
    else:
        print("Validation PASSED successfully!")
        sys.exit(0)

if __name__ == '__main__':
    validate()
