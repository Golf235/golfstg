import re

file_path = '/Users/sebastianlilliecreutz/Downloads/Home - Golfyr_files/About us - Golfyr_files/saved_resource.html' # wait, no, the file is in step 4969/content.md!
file_path = '/Users/sebastianlilliecreutz/.gemini/antigravity/brain/ddbfd671-0571-4cce-8510-9e1720ca57d2/.system_generated/steps/4969/content.md'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Let's extract the main content container of the timeline
# The section is: <section class="simple-slider-timeline-v2" ...> ... </section>
match = re.search(r'<section class="simple-slider-timeline-v2"[^>]*>(.*?)</section>', content, re.DOTALL | re.I)
if not match:
    print("Could not find simple-slider-timeline-v2 section in content!")
    # Let's search broadly
    match = re.search(r'class=["\']simple-slider-timeline-v2["\']', content)
    if match:
        print("Found class simple-slider-timeline-v2 but couldn't isolate section.")
else:
    section_html = match.group(1)
    
    # Inside this section, we have swiper-slides
    slides = re.findall(r'<div class="swiper-slide[^"]*"[^>]*>(.*?)</div>\s*</div>', section_html, re.DOTALL | re.I)
    print(f"Isolated section. Found {len(slides)} potential slides inside swiper-slide containers.")
    
    # Wait, let's find all swiper-slides inside the simpleSliderTimelineV2 swiper (excluding Thumbs)
    main_swiper_match = re.search(r'<div class="swiper simpleSliderTimelineV2">(.*?)<div class="swiper simpleSliderTimelineV2Thumbs">', section_html, re.DOTALL | re.I)
    if not main_swiper_match:
        main_swiper_match = re.search(r'<div class="swiper simpleSliderTimelineV2">(.*?)$', section_html, re.DOTALL | re.I)
        
    if main_swiper_match:
        main_swiper_html = main_swiper_match.group(1)
        # Find all swiper-slide divs
        # A slide usually ends with </div> and starts with <div class="swiper-slide ...">
        # Let's split by '<div class="swiper-slide'
        slide_parts = main_swiper_html.split('<div class="swiper-slide')
        print(f"Main Swiper parts split count: {len(slide_parts)}")
        
        for idx, part in enumerate(slide_parts[1:]):
            print(f"\n--- SLIDE {idx+1} ---")
            # Extract image src
            img_m = re.search(r'<img[^>]*src=["\']([^"\']+)["\']', part, re.I)
            # Or data-rocket-src
            if not img_m or 'svg+xml' in img_m.group(1):
                img_m = re.search(r'data-rocket-src=["\']([^"\']+)["\']', part, re.I)
            img_src = img_m.group(1) if img_m else "NO_IMAGE"
            
            # Extract year
            year_m = re.search(r'<div class="year">(\d{4})</div>', part, re.I)
            year = year_m.group(1) if year_m else "NO_YEAR"
            
            # Extract heading/title (e.g. <div class="title">...</div>)
            title_m = re.search(r'<div class="title"[^>]*>(.*?)</div>', part, re.DOTALL | re.I)
            title = title_m.group(1).strip() if title_m else "NO_TITLE"
            title = re.sub(r'<[^>]+>', '', title)
            
            # Extract description text (e.g. <div class="text">...</div> or similar)
            desc_m = re.search(r'<div class="text"[^>]*>(.*?)</div>', part, re.DOTALL | re.I)
            if not desc_m:
                desc_m = re.search(r'<p[^>]*>(.*?)</p>', part, re.DOTALL | re.I)
            desc = desc_m.group(1).strip() if desc_m else "NO_DESC"
            desc = re.sub(r'<[^>]+>', '', desc)
            desc = ' '.join(desc.split())
            
            print(f"  Year: {year}")
            print(f"  Title: {title}")
            print(f"  Image: {img_src}")
            print(f"  Description: {desc[:200]}")
