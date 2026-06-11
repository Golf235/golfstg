import re

def validate():
    # Read production.html
    with open('/Users/sebastianlilliecreutz/Downloads/Home - Golfyr_files/production.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # Find all data-translate values in HTML
    keys_in_html = set(re.findall(r'data-translate="([^"]+)"', html))
    print(f"Total unique translation keys in production.html: {len(keys_in_html)}")

    # Read rebuilt-app.js
    with open('/Users/sebastianlilliecreutz/Downloads/Home - Golfyr_files/rebuilt-app.js', 'r', encoding='utf-8') as f:
        js = f.read()

    # Extract english and german translations
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
            m = re.match(r'"([^"]+)":\s*"(.*?)",?$', line)
            if m:
                kv[m.group(1)] = m.group(2)
        return kv

    en_kv = parse_keys(en_block)
    de_kv = parse_keys(de_block)

    print(f"English keys: {len(en_kv)}")
    print(f"German keys: {len(de_kv)}")

    missing_en = []
    missing_de = []
    for key in sorted(keys_in_html):
        if key not in en_kv:
            missing_en.append(key)
        if key not in de_kv:
            missing_de.append(key)

    if missing_en:
        print(f"\nMissing English keys for production.html data-translates: {missing_en}")
    else:
        print("\nNo missing English keys for production.html!")

    if missing_de:
        print(f"Missing German keys for production.html data-translates: {missing_de}")
    else:
        print("No missing German keys for production.html!")

if __name__ == '__main__':
    validate()
