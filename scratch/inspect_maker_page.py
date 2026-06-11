from bs4 import BeautifulSoup

def inspect_html(filepath):
    print(f"\n=================== INSPECTING {filepath} ===================")
    with open(filepath, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')
    
    # Let's find headings and text near them.
    # 1. Hero
    hero_section = soup.find(class_=lambda x: x and 'hero' in x)
    if hero_section:
        print("Hero section text:")
        print(hero_section.get_text(strip=True, separator=' | ')[:500])
        
    # 2. Intro
    intro_section = soup.find(class_=lambda x: x and 'intro' in x)
    if not intro_section:
        # maybe search for a section containing "Short game" or similar? Wait, Maker is a putter. Let's see what the title is.
        # Let's find h1 or h2 elements.
        intro_section = soup.find(class_=lambda x: x and 'description' in x)
    
    # Let's just find all h2s and their following content
    for h2 in soup.find_all('h2'):
        parent = h2.parent
        print(f"\nH2: {h2.get_text(strip=True)}")
        # Print next few siblings or paragraphs
        sibling = h2.next_sibling
        count = 0
        while sibling and count < 4:
            if hasattr(sibling, 'get_text'):
                text = sibling.get_text(strip=True)
                if text:
                    print(f"  Sibling text: {text[:300]}")
                    count += 1
            sibling = sibling.next_sibling
            
        # Print some child elements if they exist
        children = h2.find_all(recursive=True)
        for c in children[:2]:
            print(f"  Child: {c.name} | {c.get_text(strip=True)}")

inspect_html("/Users/sebastianlilliecreutz/Downloads/Home - Golfyr_files/scratch/maker_en.html")
inspect_html("/Users/sebastianlilliecreutz/Downloads/Home - Golfyr_files/scratch/maker_de.html")
