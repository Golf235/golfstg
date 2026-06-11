import re

en_file = '/Users/sebastianlilliecreutz/.gemini/antigravity/brain/ddbfd671-0571-4cce-8510-9e1720ca57d2/.system_generated/steps/4969/content.md'
de_file = '/Users/sebastianlilliecreutz/.gemini/antigravity/brain/ddbfd671-0571-4cce-8510-9e1720ca57d2/.system_generated/steps/5037/content.md'

def extract_timeline_titles(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Let's extract the simple-slider-timeline-v2 section
    match = re.search(r'<section class="simple-slider-timeline-v2"[^>]*>(.*?)</section>', content, re.DOTALL | re.I)
    if not match:
        return {}
    
    section_html = match.group(1)
    
    # We want to parse the slides inside simpleSliderTimelineV2Thumbs
    thumbs_swiper_match = re.search(r'<div class="swiper simpleSliderTimelineV2Thumbs">(.*?)$', section_html, re.DOTALL | re.I)
    if not thumbs_swiper_match:
        return {}
        
    thumbs_swiper_html = thumbs_swiper_match.group(1)
    slide_parts = thumbs_swiper_html.split('<div class="swiper-slide')
    
    items = []
    for part in slide_parts[1:]:
        # Year
        year_m = re.search(r'<div class="year[^>]*>(\d{4})</div>', part, re.I)
        year = year_m.group(1) if year_m else None
        
        # Title
        title_m = re.search(r'<div class="slide-title[^>]*>(.*?)</div>', part, re.DOTALL | re.I)
        title = title_m.group(1).strip() if title_m else "NO_TITLE"
        title = re.sub(r'<[^>]+>', '', title)
        title = ' '.join(title.split())
        
        items.append({
            'year': year,
            'title': title
        })
    return items

en_titles = extract_timeline_titles(en_file)
de_titles = extract_timeline_titles(de_file)

print(f"EN titles: {len(en_titles)}, DE titles: {len(de_titles)}")

for idx, (en, de) in enumerate(zip(en_titles, de_titles)):
    print(f"Item {idx+1}: Year: {en['year']} | EN Title: '{en['title']}' | DE Title: '{de['title']}'")
