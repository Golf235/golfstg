import re

en_file = '/Users/sebastianlilliecreutz/.gemini/antigravity/brain/ddbfd671-0571-4cce-8510-9e1720ca57d2/.system_generated/steps/4969/content.md'
de_file = '/Users/sebastianlilliecreutz/.gemini/antigravity/brain/ddbfd671-0571-4cce-8510-9e1720ca57d2/.system_generated/steps/5037/content.md'

def extract_timeline_items(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Let's extract the simple-slider-timeline-v2 section
    match = re.search(r'<section class="simple-slider-timeline-v2"[^>]*>(.*?)</section>', content, re.DOTALL | re.I)
    if not match:
        return {}
    
    section_html = match.group(1)
    
    # We want to parse the slides inside simpleSliderTimelineV2 (before Thumbs)
    main_swiper_match = re.search(r'<div class="swiper simpleSliderTimelineV2">(.*?)<div class="swiper simpleSliderTimelineV2Thumbs">', section_html, re.DOTALL | re.I)
    if not main_swiper_match:
        main_swiper_match = re.search(r'<div class="swiper simpleSliderTimelineV2">(.*?)$', section_html, re.DOTALL | re.I)
        
    if not main_swiper_match:
        return {}
        
    main_swiper_html = main_swiper_match.group(1)
    slide_parts = main_swiper_html.split('<div class="swiper-slide')
    
    items = []
    for part in slide_parts[1:]:
        # Year
        year_m = re.search(r'<div class="year">(\d{4})</div>', part, re.I)
        year = year_m.group(1) if year_m else None
        
        # Desc
        desc_m = re.search(r'<div class="text"[^>]*>(.*?)</div>', part, re.DOTALL | re.I)
        if not desc_m:
            desc_m = re.search(r'<p[^>]*>(.*?)</p>', part, re.DOTALL | re.I)
        desc = desc_m.group(1).strip() if desc_m else "NO_DESC"
        desc = re.sub(r'<[^>]+>', '', desc)
        desc = ' '.join(desc.split())
        
        # Img
        img_m = re.search(r'<img[^>]*src=["\']([^"\']+)["\']', part, re.I)
        if not img_m or 'svg+xml' in img_m.group(1):
            img_m = re.search(r'data-rocket-src=["\']([^"\']+)["\']', part, re.I)
        img_src = img_m.group(1) if img_m else "NO_IMAGE"
        # Just get the filename
        img_file = img_src.split('/')[-1] if '/' in img_src else img_src
        
        items.append({
            'year': year,
            'desc': desc,
            'img': img_file
        })
    return items

en_items = extract_timeline_items(en_file)
de_items = extract_timeline_items(de_file)

print(f"EN items: {len(en_items)}, DE items: {len(de_items)}")

for idx, (en, de) in enumerate(zip(en_items, de_items)):
    print(f"\n--- ITEM {idx+1} ---")
    print(f"Year: {en['year']} | Image: {en['img']}")
    print(f"EN: {en['desc']}")
    print(f"DE: {de['desc']}")
