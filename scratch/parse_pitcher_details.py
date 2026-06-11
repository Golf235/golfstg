from bs4 import BeautifulSoup
import json

def parse_html(filepath, lang):
    print(f"\n=================== {lang} ({filepath}) ===================")
    with open(filepath, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')
    
    # 1. Intro
    intro_headline = soup.find(class_='intro-headline')
    intro_body = soup.find(class_='intro-body')
    print("Intro Headline:", intro_headline.get_text(strip=True) if intro_headline else "None")
    print("Intro Body:", intro_body.get_text(strip=True) if intro_body else "None")
    
    # 2. Why Section
    print("\nWhy Section:")
    why_section = soup.find(class_=lambda x: x and 'why-section' in x)
    if not why_section:
        # try search by word "Why"
        why_section = soup
    
    # Let's find why tab buttons and descriptions
    why_tabs = []
    # In some pages why tabs are in swiper or menu-tabs
    tabs = why_section.find_all(class_='menu-tab')
    if tabs:
        print("Tabs (menu-tabs):")
        for t in tabs:
            print("  Tab:", t.get_text(strip=True))
    
    # Text contents in the text-swiper
    content_slides = why_section.find_all(class_='content-wrapper')
    for idx, cs in enumerate(content_slides):
        title = cs.find(class_='title')
        content = cs.find(class_='content')
        title_text = title.get_text(strip=True) if title else "None"
        content_text = content.get_text(strip=True) if content else "None"
        print(f"  Slide {idx+1} Title: {title_text}")
        print(f"  Slide {idx+1} Desc: {content_text}")
        
    # 3. Where to Play
    print("\nWhere Section:")
    where_title = soup.find(class_=lambda x: x and 'where-section' in x)
    if where_title:
        h2 = where_title.find('h2')
        sub = where_title.find(class_='subtitle')
        points = where_title.find_all('li')
        print("  Title:", h2.get_text(strip=True) if h2 else "None")
        print("  Subtitle:", sub.get_text(strip=True) if sub else "None")
        print("  Points:")
        for pt in points:
            print("    -", pt.get_text(strip=True))
            
    # 4. Tech Specs
    print("\nSpecs Section:")
    specs_sec = soup.find(class_=lambda x: x and 'specs' in x)
    if specs_sec:
        items = specs_sec.find_all(class_='spec-slide')
        for item in items:
            name = item.find(class_='techspec-name')
            val = item.find(class_='techspec-value')
            desc = item.find('p')
            print(f"  - {name.get_text(strip=True) if name else 'None'}: {val.get_text(strip=True) if val else 'None'} | Desc: {desc.get_text(strip=True) if desc else 'None'}")
            
    # 5. Who is it for
    print("\nWho Section:")
    # Look for who section background image
    who_sec = soup.find(id='for-who')
    if not who_sec:
        who_sec = soup.find(class_=lambda x: x and 'for-who' in x)
    if who_sec:
        head = who_sec.find(class_='head')
        body = who_sec.find(class_='additional-content')
        print("  Title:", head.get_text(separator=' ', strip=True) if head else "None")
        print("  Body:", body.get_text(strip=True) if body else "None")
        
        # Check inline styles for background image
        style = who_sec.get('style', '')
        print("  Style:", style)

parse_html("scratch/pitcher_en.html", "ENGLISH")
parse_html("scratch/pitcher_de.html", "GERMAN")
