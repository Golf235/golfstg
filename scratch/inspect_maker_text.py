import re

def search_text(filepath, lang):
    print(f"\n=================== TEXT SEARCH: {lang} ===================")
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Let's extract all <h1, <h2, <h3 tags and paragraphs <p, and list items <li
    # Let's find tags using regex
    pattern = re.compile(r'<(h1|h2|h3|p|li|div)[^>]*>(.*?)</\1>', re.DOTALL | re.IGNORECASE)
    matches = pattern.findall(content)
    
    print("Cleaned text snippets matching key concepts:")
    for tag, inner_text in matches:
        # clean HTML tags inside inner_text
        text_clean = re.sub(r'<[^>]+>', ' ', inner_text)
        text_clean = re.sub(r'\s+', ' ', text_clean).strip()
        
        if not text_clean:
            continue
            
        # If it's a heading or interesting paragraph, print it
        if tag in ('h1', 'h2', 'h3'):
            print(f"[{tag.upper()}] {text_clean}")
        elif any(keyword in text_clean.lower() for keyword in [
            'maker', 'precision', 'green', 'putt', 'stability', 'sweet spot', 'roll', 'balance', 'mallet', 'vibration',
            'präzision', 'grün', 'stabilität', 'schwerpunkt', 'toleranz', 'schwunggewicht', 'putten'
        ]):
            if len(text_clean) > 30:
                print(f"  ({tag}) {text_clean[:200]}...")

search_text("/Users/sebastianlilliecreutz/Downloads/Home - Golfyr_files/scratch/maker_en.html", "ENGLISH")
search_text("/Users/sebastianlilliecreutz/Downloads/Home - Golfyr_files/scratch/maker_de.html", "GERMAN")
