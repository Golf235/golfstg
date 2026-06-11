import re

filepath = '/Users/sebastianlilliecreutz/.gemini/antigravity/brain/ddbfd671-0571-4cce-8510-9e1720ca57d2/.system_generated/steps/4969/content.md'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

match = re.search(r'<div class="swiper simpleSliderTimelineV2Thumbs">(.*?)$', content, re.DOTALL | re.I)
if match:
    swiper_html = match.group(1)
    # Split by class="swiper-slide
    slides = swiper_html.split('<div class="swiper-slide')
    print(f"Total slides found in Thumbs Swiper: {len(slides)-1}")
    for idx, slide in enumerate(slides[14:]):
        print(f"\n--- EXTRA SLIDE {idx+14} ---")
        print(slide[:1000])
