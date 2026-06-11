import os
import re

workspace_dir = '/Users/sebastianlilliecreutz/Downloads/Home - Golfyr_files'
about_dir = os.path.join(workspace_dir, 'About us - Golfyr_files')

# Files to extract from
files_to_check = [
    ('main-1920.css', about_dir),
    ('main-phase-2.css', about_dir),
    ('main-phase-3.css', about_dir),
    ('sliders.css', about_dir)
]

selectors_to_extract = [
    r'\.simple-slider-makers\b',
    r'\.simple-slider-timeline-v2\b',
    r'\.numbers-and-data-entry\b',
    r'\.slider-tabs-nav\b',
    r'\.quote-with-image\b',
    r'\.quote-with-image-v4\b',
    r'\.simpleSliderTimelineV2\b',
    r'\.simpleSliderTimelineV2Thumbs\b',
    r'\.simpleSliderTabNav\b',
    r'\.simpleSliderTabNavContent\b',
    r'\.simpleSliderMakers\b',
    r'\.menu-tab\b',
    r'\.empty-slide-timeline\b',
    r'\.last-swipe\b'
]

# Let's write a parser that extracts CSS rule blocks.
# A CSS rule block typically starts with selectors, followed by '{', and ends with '}' matching the balance.
# We also have media queries: `@media ... { ... }` which can contain multiple rules.
# If a rule block contains one of our target selectors, we want to extract it.
# To be robust, let's parse the CSS text character by character to identify top-level blocks and nested blocks (media queries).

def extract_matching_rules(css_text, pattern_list):
    extracted_parts = []
    
    # We will find top-level blocks: rule sets or media queries.
    # A block starts at some character and ends when braces are balanced.
    pos = 0
    length = len(css_text)
    
    while pos < length:
        # Skip whitespaces/comments
        if css_text[pos:pos+2] == '/*':
            comment_end = css_text.find('*/', pos+2)
            if comment_end == -1:
                break
            pos = comment_end + 2
            continue
            
        if css_text[pos].isspace():
            pos += 1
            continue
            
        # Find start of block
        block_start = pos
        brace_start = css_text.find('{', pos)
        if brace_start == -1:
            break
            
        # Balance braces to find block end
        brace_count = 0
        block_end = -1
        for idx in range(brace_start, length):
            char = css_text[idx]
            if char == '{':
                brace_count += 1
            elif char == '}':
                brace_count -= 1
                if brace_count == 0:
                    block_end = idx + 1
                    break
        
        if block_end == -1:
            # Unbalanced block, just break
            break
            
        block_content = css_text[block_start:block_end]
        
        # Check if block matches any patterns
        # If it's a media query, we might want to check its inner content or check if the whole media query matches any pattern
        is_match = False
        
        # If it's a media query, let's extract matching inner rule sets or just match the whole media query if it contains any selector.
        # Actually, extracting matching inner rule sets of media queries is cleaner, but keeping the media query structure is crucial.
        # Let's see: if the block starts with '@media', parse its inner blocks.
        if block_content.strip().startswith('@media'):
            # Parse media query inner rules
            header_end = block_content.find('{')
            media_header = block_content[:header_end+1]
            media_body = block_content[header_end+1:-1]
            
            inner_rules = extract_matching_rules(media_body, pattern_list)
            if inner_rules.strip():
                extracted_parts.append(media_header + "\n" + inner_rules + "}\n")
        else:
            # Regular rule block
            selector = block_content[:block_content.find('{')].strip()
            for pat in pattern_list:
                if re.search(pat, selector):
                    is_match = True
                    break
            if is_match:
                extracted_parts.append(block_content + "\n")
                
        pos = block_end
        
    return "".join(extracted_parts)

output_css = []
for filename, folder in files_to_check:
    filepath = os.path.join(folder, filename)
    if not os.path.exists(filepath):
        continue
    print(f"Processing {filename}...")
    with open(filepath, 'r', encoding='utf-8') as f:
        css_text = f.read()
    
    extracted = extract_matching_rules(css_text, selectors_to_extract)
    if extracted.strip():
        output_css.append(f"\n\n/* ==================================================\n   Extracted from {filename}\n   ================================================== */\n")
        output_css.append(extracted)

rebuilt_style_path = os.path.join(workspace_dir, 'rebuilt-style.css')
with open(rebuilt_style_path, 'a', encoding='utf-8') as f:
    f.write("".join(output_css))

print(f"Appended extracted About Us styles to {rebuilt_style_path}")
