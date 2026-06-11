import re

filepath = '/Users/sebastianlilliecreutz/Downloads/Home - Golfyr_files/About us - Golfyr_files/parsed_sections/section_5_simple-slider-timeline-v2_no_id.html'
with open(filepath, 'r', encoding='utf-8') as f:
    html = f.read()

# Let's see the outer structure of the section
# We can print the first 2000 chars of the html
print("=== TIMELINE OUTER STRUCTURE ===")
print(html[:2000])

# Let's search for controls (buttons, scrollbar, pagination etc)
print("\n=== TIMELINE CONTROLS ===")
controls = re.findall(r'<div class="swiper-button-[^>]*>|<div class="swiper-scrollbar[^>]*>|<div class="swiper-pagination[^>]*>', html, re.I)
for c in controls:
    print(c)
