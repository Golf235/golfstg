import urllib.request
import re
from html.parser import HTMLParser

class TextExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.in_spec = False
        self.current_text = []
        
    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)
        # Check if we are inside a spec slide or specs container
        if tag == 'div' and ('spec' in attrs_dict.get('class', '') or 'techspec' in attrs_dict.get('class', '')):
            self.in_spec = True
            
    def handle_endtag(self, tag):
        if tag == 'div' and self.in_spec:
            text = " ".join(self.current_text).strip()
            if text:
                print(f"Spec Content: {text}")
            self.current_text = []
            self.in_spec = False
            
    def handle_data(self, data):
        if self.in_spec:
            cleaned = data.strip()
            if cleaned:
                self.current_text.append(cleaned)

# Fetch English page
url_en = "https://golfyr.com/sevenclubgame/the-mover/?v=d88fc6edf21e"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

print("=== ENGLISH SPECS ===")
req = urllib.request.Request(url_en, headers=headers)
try:
    with urllib.request.urlopen(req) as response:
        html = response.read().decode('utf-8')
    parser = TextExtractor()
    parser.feed(html)
except Exception as e:
    print(f"Error: {e}")

# Fetch German page (usually via /de/ or language cookie or ?lang=de)
# Let's try to search the html for any German text or see how the site handles languages.
# Let's also print all paragraphs containing "volume" or "240" or "cc"
print("\n=== SEARCHING FOR VOLUME OR 240 ===")
if 'html' in locals():
    for line in html.split('\n'):
        if '240' in line or 'volume' in line or 'Volume' in line or 'cc' in line:
            print(line.strip())
