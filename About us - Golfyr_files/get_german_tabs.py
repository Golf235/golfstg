import re

de_file = '/Users/sebastianlilliecreutz/.gemini/antigravity/brain/ddbfd671-0571-4cce-8510-9e1720ca57d2/.system_generated/steps/5037/content.md'

with open(de_file, 'r', encoding='utf-8') as f:
    de_html = f.read()

# Let's search for simpleSliderTabNavContent in German html
match = re.search(r'<div class="swiper simpleSliderTabNavContent">(.*?)</div>\s*</div>\s*</div>\s*</div>\s*</div>\s*</div>', de_html, re.DOTALL | re.I)
if not match:
    # Try finding simpleSliderTabNavContent and getting all swiper-slides after it
    match = re.search(r'simpleSliderTabNavContent.*?swiper-wrapper(.*?)</div>\s*</div>\s*</div>', de_html, re.DOTALL | re.I)

if match:
    swiper_html = match.group(1)
    slides = swiper_html.split('<div class="swiper-slide')
    for idx, slide in enumerate(slides[1:]):
        title_m = re.search(r'<div class="title"[^>]*>(.*?)</div>', slide, re.DOTALL | re.I)
        desc_m = re.search(r'<div class="content"[^>]*>(.*?)</div>', slide, re.DOTALL | re.I)
        title = re.sub(r'<[^>]+>', '', title_m.group(1)).strip() if title_m else "NO_TITLE"
        desc = re.sub(r'<[^>]+>', '', desc_m.group(1)).strip() if desc_m else "NO_DESC"
        print(f"Slide {idx+1}: Title: {title} | Desc: {desc}")
else:
    # Just search for the titles and contents inside simpleSliderTabNavContent
    print("Could not isolate simpleSliderTabNavContent wrapper. Let's list occurrences of content-wrapper:")
    wrappers = re.findall(r'<div class="content-wrapper">(.*?)</div>\s*</div>', de_html, re.DOTALL | re.I)
    for idx, wrap in enumerate(wrappers):
        title_m = re.search(r'<div class="title"[^>]*>(.*?)</div>', wrap, re.DOTALL | re.I)
        desc_m = re.search(r'<div class="content"[^>]*>(.*?)</div>', wrap, re.DOTALL | re.I)
        title = re.sub(r'<[^>]+>', '', title_m.group(1)).strip() if title_m else "NO_TITLE"
        desc = re.sub(r'<[^>]+>', '', desc_m.group(1)).strip() if desc_m else "NO_DESC"
        print(f"Wrapper {idx+1}: Title: {title} | Desc: {desc}")
