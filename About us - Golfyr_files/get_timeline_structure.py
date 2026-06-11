with open('/Users/sebastianlilliecreutz/Downloads/Home - Golfyr_files/About us - Golfyr_files/parsed_sections/section_5_simple-slider-timeline-v2_no_id.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Let's find simpleSliderTimelineV2Thumbs start and print about 3000 chars from there
idx = html.find('simpleSliderTimelineV2Thumbs')
if idx != -1:
    print("=== THUMBS STRUCTURE ===")
    print(html[idx-100:idx+4000])
else:
    print("Could not find simpleSliderTimelineV2Thumbs in html.")
