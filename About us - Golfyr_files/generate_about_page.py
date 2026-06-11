import os
import re

workspace_dir = '/Users/sebastianlilliecreutz/Downloads/Home - Golfyr_files'
about_dir = os.path.join(workspace_dir, 'About us - Golfyr_files')
parsed_dir = os.path.join(about_dir, 'parsed_sections')

# We will load the sections in order
section_files = [
    'section_1_hero-video-home-p1_d-flex_flex-column_justify-content-end_no_id.html',
    'section_2_large-text-block_top-md_bottom-md_no_id.html',
    'section_3_slider-tabs-nav_no_id.html',
    'section_4_content-spacer_height-md_no_id.html',
    'section_5_simple-slider-timeline-v2_no_id.html',
    'section_6_large-text-block_top-lg_bottom-lg_no_id.html',
    'section_7_container_quote-with-image_quote-with-image-v4_no_id.html',
    'section_8_content-spacer_height-md_no_id.html',
    'section_9_simple-slider-makers_makers.html',
    'section_10_responsive-image-content_short-height-mobile_no_id.html',
    'section_11_numbers-and-data-entry_no_id.html',
    'section_12_quote-with-image_no_id.html'
]

sections_html = []

for filename in section_files:
    filepath = os.path.join(parsed_dir, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # Let's perform general cleaning and replacements for this section
    
    # 1. Clean Lazy Loading images and Noscript tags, replace with simple responsive images
    # Usually we have structures like:
    # <img src="data:image/svg..." data-lazy-src="URL" class="img-fluid" ...> <noscript><img src="URL" ...></noscript>
    # We want to replace it with a clean single image:
    # <img src="./About us - Golfyr_files/IMAGE_NAME" class="img-fluid" ...>
    # First, let's extract the actual image source (from data-lazy-src or src inside noscript)
    
    # Let's do regex replacement of the noscript block and lazy src
    # Simplify <noscript>...<img ... src="URL" ...>...</noscript> to empty, and update the primary image src
    # But since it can be complex, let's write a targeted regex replacement for images:
    
    # Let's look for lazy-loaded images:
    # <img ... src="data:image/svg+xml..." ... data-lazy-src="HTTPS_URL" ...>
    # We will rewrite them to use local paths under ./About us - Golfyr_files/
    def clean_image_tag(match):
        img_tag = match.group(0)
        # Find lazy-srcset or srcset
        srcset = ""
        srcset_m = re.search(r'data-lazy-srcset="([^"]+)"', img_tag)
        if not srcset_m:
            srcset_m = re.search(r'srcset="([^"]+)"', img_tag)
        if srcset_m:
            srcset = srcset_m.group(1)
            # Rewrite URLs in srcset to local
            urls = re.findall(r'(https://golfyr\.com/wp-content/uploads/\d{4}/\d{2}/([^,\s\)]+\.(?:jpg|png|jpeg)))', srcset)
            for full_url, filename in urls:
                srcset = srcset.replace(full_url, f'./About us - Golfyr_files/{filename}')
        
        # Find lazy-src or src
        src = ""
        src_m = re.search(r'data-lazy-src="([^"]+)"', img_tag)
        if not src_m:
            src_m = re.search(r'src="([^"]+)"', img_tag)
        if src_m:
            src = src_m.group(1)
            if 'svg+xml' in src:
                # Find from noscript or somewhere else
                pass
            else:
                url_filename = src.split('/')[-1] if '/' in src else src
                src = f'./About us - Golfyr_files/{url_filename}'
                
        # If src is still data:image/svg, let's extract the correct source from the filename attributes or somewhere
        if 'data:image/svg' in src or not src:
            # Let's look for alt/class or regex matches of wp-content
            wp_m = re.search(r'https://golfyr\.com/wp-content/uploads/\d{4}/\d{2}/([^"\s>]+)', img_tag)
            if wp_m:
                src = f'./About us - Golfyr_files/{wp_m.group(1)}'
        
        # Now construct a clean image tag
        # Find class
        class_m = re.search(r'class="([^"]+)"', img_tag)
        cls_str = f'class="{class_m.group(1)}"' if class_m else 'class="img-fluid"'
        
        # Find alt
        alt_m = re.search(r'alt="([^"]+)"', img_tag)
        alt_str = f'alt="{alt_m.group(1)}"' if alt_m else 'alt="Golfyr Image"'
        
        # Find width/height
        w_m = re.search(r'width="([^"]+)"', img_tag)
        h_m = re.search(r'height="([^"]+)"', img_tag)
        dim_str = ""
        if w_m and h_m:
            dim_str = f'width="{w_m.group(1)}" height="{h_m.group(1)}"'
            
        srcset_str = f'srcset="{srcset}"' if srcset else ""
        
        new_tag = f'<img src="{src}" {cls_str} {alt_str} {dim_str} {srcset_str} decoding="async">'
        return new_tag

    # Remove noscript tags completely first to avoid duplicates
    html = re.sub(r'<noscript>.*?</noscript>', '', html, flags=re.DOTALL | re.I)
    # Clean image tags
    html = re.sub(r'<img\b[^>]*>', clean_image_tag, html, flags=re.I)
    
    # 2. Add translation data tags based on the section
    if 'hero-video-home-p1' in filename:
        html = html.replace('Welcome to<br>our World', 'Welcome to<br>our World') # title
        html = html.replace('Welcome to<br>our World', '<span data-translate="about-hero-title">Welcome to<br>our World</span>')
        html = html.replace('Discover more', '<span data-translate="about-scroll-cta">Discover more</span>')
        html = html.replace('Get to know us', 'Get to know us')
        html = html.replace('Get to know us</a>', '<span data-translate="about-hero-btn">Get to know us</span></a>')
        
    elif 'large-text-block_top-md_bottom-md' in filename:
        html = html.replace('<p>Based in Switzerland, we are redefining the way golf is played. We call it 7&gt;14: an optimized golf experience using only seven essential SWISS MADE carbon clubs on the course.</p>',
                            '<p data-translate="about-intro-text">Based in Switzerland, we are redefining the way golf is played. We call it 7&gt;14: an optimized golf experience using only seven essential SWISS MADE carbon clubs on the course.</p>')
        
    elif 'slider-tabs-nav' in filename:
        html = html.replace('<p>Our Values</p>', '<p data-translate="about-values-title">Our Values</p>')
        html = html.replace('<h2 class="content"><p><span dir="ltr" role="presentation">Our approach makes golf simpler, more accessible, and more enjoyable—</span><span dir="ltr" role="presentation">bringing back the pure joy of the game. It’s time to rethink golf.</span></p></h2>',
                            '<h2 class="content"><p data-translate="about-values-subtitle"><span dir="ltr" role="presentation">Our approach makes golf simpler, more accessible, and more enjoyable—</span><span dir="ltr" role="presentation">bringing back the pure joy of the game. It’s time to rethink golf.</span></p></h2>')
        
        # Tabs
        html = html.replace('<div class="menu-tab">Joy</div>', '<div class="menu-tab" data-translate="about-value-joy-title">Joy</div>')
        html = html.replace('<div class="menu-tab">Simplicity</div>', '<div class="menu-tab" data-translate="about-value-simplicity-title">Simplicity</div>')
        html = html.replace('<div class="menu-tab">Quality</div>', '<div class="menu-tab" data-translate="about-value-quality-title">Quality</div>')
        html = html.replace('<div class="menu-tab">Technology</div>', '<div class="menu-tab" data-translate="about-value-technology-title">Technology</div>')
        html = html.replace('<div class="menu-tab">Performance</div>', '<div class="menu-tab" data-translate="about-value-performance-title">Performance</div>')
        
        # Slides texts
        # Joy
        html = html.replace('<div class="title">\n                          <p>Joy</p>                        </div>\n                        <div class="content">\n                          <p>Golf is meant to be fun. We focus on effortless play and pure enjoyment.</p>                        </div>',
                            '<div class="title">\n                          <p data-translate="about-value-joy-title">Joy</p>                        </div>\n                        <div class="content">\n                          <p data-translate="about-value-joy-desc">Golf is meant to be fun. We focus on effortless play and pure enjoyment.</p>                        </div>')
        # Simplicity
        html = html.replace('<div class="title">\n                          <p>Simplicity</p>                        </div>\n                        <div class="content">\n                          <p><span dir="ltr" role="presentation">Less complexity, more game. Our clubs streamline the experience, </span><span dir="ltr" role="presentation">making golf easier and more intuitive.</span></p>                        </div>',
                            '<div class="title">\n                          <p data-translate="about-value-simplicity-title">Simplicity</p>                        </div>\n                        <div class="content">\n                          <p data-translate="about-value-simplicity-desc"><span dir="ltr" role="presentation">Less complexity, more game. Our clubs streamline the experience, </span><span dir="ltr" role="presentation">making golf easier and more intuitive.</span></p>                        </div>')
        # Quality
        html = html.replace('<div class="title">\n                          <p>Quality</p>                        </div>\n                        <div class="content">\n                          <p>Precision and reliability, perfected through Swiss Engineering.</p>                        </div>',
                            '<div class="title">\n                          <p data-translate="about-value-quality-title">Quality</p>                        </div>\n                        <div class="content">\n                          <p data-translate="about-value-quality-desc">Precision and reliability, perfected through Swiss Engineering.</p>                        </div>')
        # Technology
        html = html.replace('<div class="title">\n                          <p>Technology</p>                        </div>\n                        <div class="content">\n                          <p><span dir="ltr" role="presentation">With Carbonics Technology, we’re redefining club design and </span><span dir="ltr" role="presentation">performance.</span></p>                        </div>',
                            '<div class="title">\n                          <p data-translate="about-value-technology-title">Technology</p>                        </div>\n                        <div class="content">\n                          <p data-translate="about-value-technology-desc"><span dir="ltr" role="presentation">With Carbonics Technology, we’re redefining club design and </span><span dir="ltr" role="presentation">performance.</span></p>                        </div>')
        # Performance
        html = html.replace('<div class="title">\n                          <p>Performance</p>                        </div>\n                        <div class="content">\n                          <p>Maximum efficiency and better results for a sustainably optimized game.</p>                        </div>',
                            '<div class="title">\n                          <p data-translate="about-value-performance-title">Performance</p>                        </div>\n                        <div class="content">\n                          <p data-translate="about-value-performance-desc">Maximum efficiency and better results for a sustainably optimized game.</p>                        </div>')
        
    elif 'simple-slider-timeline-v2' in filename:
        html = html.replace('<div class="title">Explore our story</div>', '<div class="title" data-translate="about-timeline-title">Explore our story</div>')
        
        timeline_titles_map = {
            "An innovator with a vision": 1,
            "Proof of Idea": 2,
            "Proof of Concept": 3,
            "Club development": 4,
            "Proof of Market Fit": 5,
            "Proof of Concept #sevenclubgame": 6,
            "Groove Days & Field Tests": 7,
            "Groove Days &amp; Field Tests": 7,
            "Performance & Durability Testing": 8,
            "Performance &amp; Durability Testing": 8,
            "Robot Test in San Diego": 9,
            "Certified for Tournament Play": 10,
            "Market Launch of the Maker": 11,
            "The Maker at LIV Golf": 12,
            "Full Set Unveiled: Field Tests Begin": 13
        }
        
        def replace_timeline_slide(match):
            full_match = match.group(0)
            order_attr = match.group(1) or ""
            title = match.group(2).strip()
            desc = match.group(3)
            
            idx = timeline_titles_map.get(title)
            if not idx:
                norm_title = title.replace('&amp;', '&')
                idx = timeline_titles_map.get(norm_title)
                
            if idx:
                title_tag = f'<div class="slide-title{order_attr}" data-translate="about-timeline-m{idx}-title">{title}</div>'
                desc_tag = f'<div class="slide-content"><p data-translate="about-timeline-m{idx}-desc">{desc}</p></div>'
                return f'{title_tag}\n                                                                                                                {desc_tag}'
            return full_match

        pattern = r'<div class="slide-title( order-2)?">([^<]+)</div>\s*<div class="slide-content"><p>(.*?)</p></div>'
        html = re.sub(pattern, replace_timeline_slide, html, flags=re.DOTALL)
        
        # Last swipe
        html = html.replace('<div class="year order-1">Our story continues&#8230;</div>',
                            '<div class="year order-1" data-translate="about-timeline-continue">Our story continues&#8230;</div>')
        
    elif 'large-text-block_top-lg_bottom-lg' in filename:
        html = html.replace('<p>Seven clubs instead of 14 means more focus and clarity. Enjoy the course without the burden of excessive gear – and experience the game you truly love, developed by four visionary minds.</p>',
                            '<p data-translate="about-visionaries-text">Seven clubs instead of 14 means more focus and clarity. Enjoy the course without the burden of excessive gear – and experience the game you truly love, developed by four visionary minds.</p>')
        
    elif 'quote-with-image-v4' in filename:
        html = html.replace('“Golf is a fascinating game which is best played with a light heart, good friends and continuous improvement.”',
                            '<span data-translate="about-roger-quote">“Golf is a fascinating game which is best played with a light heart, good friends and continuous improvement.”</span>')
        html = html.replace('Roger Stadler', '<span data-translate="about-roger-name">Roger Stadler</span>')
        html = html.replace('FOUNDER/PRESIDENT OF THE BOARD', '<span data-translate="about-roger-role">FOUNDER/PRESIDENT OF THE BOARD</span>')
        
    elif 'simple-slider-makers' in filename:
        # Daniel Hüsler
        html = html.replace('<p>&#8220;Our hard work pays off and the statistics prove it: You will land on the fairway more often and with a lot more fun.&#8221;</p>',
                            '<p data-translate="about-daniel-quote">&#8220;Our hard work pays off and the statistics prove it: You will land on the fairway more often and with a lot more fun.&#8221;</p>')
        html = html.replace('Daniel Hüsler', '<span data-translate="about-daniel-name">Daniel Hüsler</span>')
        html = html.replace('HEAD OF TECHNOLOGY', '<span data-translate="about-daniel-role">HEAD OF TECHNOLOGY</span>')
        
        # Alfredo Häberli
        html = html.replace('<p>&#8220;You must ask the right questions to create something outstanding. This time it was: What needs to be reduced?&#8221;</p>',
                            '<p data-translate="about-alfredo-quote">&#8220;You must ask the right questions to create something outstanding. This time it was: What needs to be reduced?&#8221;</p>')
        html = html.replace('Alfredo Häberli', '<span data-translate="about-alfredo-name">Alfredo Häberli</span>')
        # Alfredo Häberli has no role on the card in the original scrape? Let's check:
        # Looking at Section 9 code, lines 50-51 has: <div class="function order-2 order-lg-3">CREATIVE DIRECTOR</div>
        html = html.replace('CREATIVE DIRECTOR', '<span data-translate="about-alfredo-role">CREATIVE DIRECTOR</span>')
        
        # Olivier Widrig
        html = html.replace('<p>&#8220;It’s finally time to rethink golf and enabling a more playful approach to the game as originally intended. When you’re on the course with a Golfyr set the tale will tell itself.&#8221;</p>',
                            '<p data-translate="about-olivier-quote">&#8220;It’s finally time to rethink golf and enabling a more playful approach to the game as originally intended. When you’re on the course with a Golfyr set the tale will tell itself.&#8221;</p>')
        html = html.replace('Olivier Widrig', '<span data-translate="about-olivier-name">Olivier Widrig</span>')
        html = html.replace('HEAD OF GOLF', '<span data-translate="about-olivier-role">HEAD OF GOLF</span>')
        
    elif 'numbers-and-data-entry' in filename:
        html = html.replace('300&#8217;000', '<span data-translate="about-stats-n1-val">300’000</span>')
        html = html.replace('200', '<span data-translate="about-stats-n2-val">200</span>')
        html = html.replace('7', '<span data-translate="about-stats-n3-val">7</span>')
        
        html = html.replace('<p>shots on the golf club face at speeds of up to 195 km/h.</p>',
                            '<p data-translate="about-stats-n1-text">shots on the golf club face at speeds of up to 195 km/h.</p>')
        html = html.replace('<p>manufacturing steps to produce the finished golf club.</p>',
                            '<p data-translate="about-stats-n2-text">manufacturing steps to produce the finished golf club.</p>')
        html = html.replace('<p>years to create the full carbon clubs with their unique performance profile.</p>',
                            '<p data-translate="about-stats-n3-text">years to create the full carbon clubs with their unique performance profile.</p>')
        
    elif 'section_12_quote-with-image' in filename:
        html = html.replace('<p>&#8220;It is not about the difficulties you overcome but about the fun you have while pursuing your vision.&#8221;</p>',
                            '<p data-translate="about-marcel-quote">&#8220;It is not about the difficulties you overcome but about the fun you have while pursuing your vision.&#8221;</p>')
        html = html.replace('<p>Marcel Lendenmann</p>', '<p data-translate="about-marcel-name">Marcel Lendenmann</p>')
        html = html.replace('<p>CEO</p>', '<p data-translate="about-marcel-role">CEO</p>')
        html = html.replace('Get in contact with us</a>', '<span data-translate="about-marcel-btn">Get in contact with us</span></a>')
        html = html.replace('href="https://golfyr.com/contact/"', 'href="./index.html#contact"')
        
    sections_html.append(html)

all_sections_content = "\n\n".join(sections_html)

# Now let's open index.html to inherit its header and footer markup
index_path = os.path.join(workspace_dir, 'index.html')
with open(index_path, 'r', encoding='utf-8') as f:
    index_content = f.read()

# We want to extract:
# 1. Everything from <!DOCTYPE html> to <header> (excluding <header>)
# 2. The <header> to </header> block
# 3. The <footer> to </footer> block
# 4. The mobile drawer <div class="mobile-menu"> ... </div>
# 5. The closing scripts and tags at the bottom

# Let's extract them using regex or split
header_start = index_content.find('<header>')
header_end = index_content.find('</header>') + len('</header>')

head_content = index_content[:header_start]
header_content = index_content[header_start:header_end]

# Footer
footer_start = index_content.find('<footer>')
footer_end = index_content.find('</footer>') + len('</footer>')
footer_content = index_content[footer_start:footer_end]

# Mobile menu
mobile_menu_start = index_content.find('<div class="mobile-menu">')
# Find balanced closing div for mobile-menu
brace_count = 0
mobile_menu_end = -1
for i in range(mobile_menu_start, len(index_content)):
    sub = index_content[i:i+5]
    if sub == '<div ':
        brace_count += 1
    elif index_content[i:i+6] == '</div>':
        brace_count -= 1
        if brace_count == 0:
            mobile_menu_end = i + 6
            break

mobile_menu_content = index_content[mobile_menu_start:mobile_menu_end]

# Scripts and closing body/html
scripts_content = index_content[footer_end:]

# Update page title
head_content = re.sub(r'<title>[^<]+</title>', '<title>About us - Golfyr</title>', head_content)

# Reassemble about.html
about_html_content = f"""{head_content}
{header_content}

<main>
{all_sections_content}
</main>

{footer_content}

{mobile_menu_content}

{scripts_content}
"""

# Let's clean up any layout issues or paths
about_html_content = about_html_content.replace('href="#makers"', 'href="#makers"') # hero button anchor

# Highlight active menu items for About Us page
about_html_content = about_html_content.replace(
    '<li><a href="./about.html" data-translate="nav-about">About</a></li>',
    '<li><a href="./about.html" data-translate="nav-about" class="active">About</a></li>'
)

# Write to file
about_path = os.path.join(workspace_dir, 'about.html')
with open(about_path, 'w', encoding='utf-8') as f:
    f.write(about_html_content)

print(f"Generated {about_path} successfully!")
