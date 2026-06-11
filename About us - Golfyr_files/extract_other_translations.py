import re

en_file = '/Users/sebastianlilliecreutz/.gemini/antigravity/brain/ddbfd671-0571-4cce-8510-9e1720ca57d2/.system_generated/steps/4969/content.md'
de_file = '/Users/sebastianlilliecreutz/.gemini/antigravity/brain/ddbfd671-0571-4cce-8510-9e1720ca57d2/.system_generated/steps/5037/content.md'

with open(en_file, 'r', encoding='utf-8') as f:
    en_html = f.read()

with open(de_file, 'r', encoding='utf-8') as f:
    de_html = f.read()

# Let's extract sections using regex
def get_sections(content):
    # Regex to find <section class="xxx" id="yyy"> ... </section>
    sections = re.findall(r'<section\s+class=["\']([^"\']+)["\'][^>]*>(.*?)</section>', content, re.DOTALL | re.I)
    result = {}
    for cls, body in sections:
        if 'simple-slider-timeline-v2' in cls or 'content-spacer' in cls:
            continue
        # Extract text in tags
        tags = re.findall(r'<[a-zA-Z0-9]+[^>]*>(.*?)</[a-zA-Z0-9]+>', body, re.DOTALL | re.I)
        texts = []
        for t in tags:
            t_clean = re.sub(r'<[^>]+>', '', t).strip()
            # Unescape html entities
            t_clean = t_clean.replace('&#8220;', '“').replace('&#8221;', '”').replace('&#8217;', '’').replace('&amp;', '&').replace('&nbsp;', ' ')
            t_clean = ' '.join(t_clean.split())
            if len(t_clean) > 3 and t_clean not in texts and not t_clean.startswith('<'):
                texts.append(t_clean)
        result[cls] = texts
    return result

en_dict = get_sections(en_html)
de_dict = get_sections(de_html)

for cls, texts in en_dict.items():
    print(f"\nSection: {cls}")
    de_texts = de_dict.get(cls, [])
    print("  EN:")
    for t in texts[:6]:
        print(f"    - {t}")
    print("  DE:")
    for t in de_texts[:6]:
        print(f"    - {t}")
