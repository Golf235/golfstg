import urllib.request
import re
from html.parser import HTMLParser

class RiserParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.in_title = False
        self.in_body = False
        self.in_spec = False
        self.current_text = []
        
    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)
        
        # Capture image elements
        if tag == 'img':
            src = attrs_dict.get('src')
            data_src = attrs_dict.get('data-src')
            alt = attrs_dict.get('alt')
            print(f"IMG: src={src}, data-src={data_src}, alt={alt}")
        elif tag == 'source':
            srcset = attrs_dict.get('srcset')
            data_srcset = attrs_dict.get('data-srcset')
            print(f"SOURCE: srcset={srcset}, data-srcset={data_srcset}")
            
        # Identify specifications and translation details
        if tag == 'div' and ('spec' in attrs_dict.get('class', '') or 'techspec' in attrs_dict.get('class', '')):
            self.in_spec = True
            
        style = attrs_dict.get('style')
        if style and 'url' in style:
            print(f"STYLE BACKGROUND: {style}")
            
    def handle_endtag(self, tag):
        if tag == 'div' and self.in_spec:
            text = " ".join(self.current_text).strip()
            if text:
                print(f"SPEC TEXT: {text}")
            self.current_text = []
            self.in_spec = False
            
    def handle_data(self, data):
        if self.in_spec:
            cleaned = data.strip()
            if cleaned:
                self.current_text.append(cleaned)

# Fetch English Riser page
url_en = "https://golfyr.com/sevenclubgame/the-riser/?v=d88fc6edf21e"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

print("=== FETCHING ENGLISH RISER PAGE ===")
req = urllib.request.Request(url_en, headers=headers)
try:
    with urllib.request.urlopen(req) as response:
        html_en = response.read().decode('utf-8')
    parser = RiserParser()
    parser.feed(html_en)
except Exception as e:
    print(f"Error English: {e}")

# Fetch German Riser page
url_de = "https://golfyr.com/de/sevenclubgame/the-riser/"
print("\n=== FETCHING GERMAN RISER PAGE ===")
req_de = urllib.request.Request(url_de, headers=headers)
try:
    with urllib.request.urlopen(req_de) as response:
        html_de = response.read().decode('utf-8')
except Exception as e:
    print(f"Error German: {e}")
    html_de = None

# Extracting translations & text patterns
if 'html_en' in locals():
    print("\n=== SEARCHING FOR SPECIFIC TEXT PATTERNS (EN) ===")
    # Search for descriptions and spec values
    for line in html_en.split('\n'):
        if any(keyword in line for keyword in ['24°', '23°', '25°', '26°', 'riser', 'Riser', 'loft', 'swing weight', 'volume']):
            line_clean = line.strip()
            if len(line_clean) < 300 and line_clean:
                print(f"EN Line: {line_clean}")

if html_de:
    print("\n=== SEARCHING FOR SPECIFIC TEXT PATTERNS (DE) ===")
    for line in html_de.split('\n'):
        if any(keyword in line for keyword in ['24°', '23°', '25°', '26°', 'riser', 'Riser', 'loft', 'Volumen']):
            line_clean = line.strip()
            if len(line_clean) < 300 and line_clean:
                print(f"DE Line: {line_clean}")
