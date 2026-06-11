import urllib.request
import re
from html.parser import HTMLParser

class DataExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.tags_stack = []
        self.current_class = ""
        self.in_why_tabs = False
        self.in_why_desc = False
        self.in_specs = False
        self.specs_data = []
        self.in_intro = False
        self.intro_text = []
        
    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)
        self.tags_stack.append((tag, attrs_dict))
        
        # Check image files
        if tag == 'img':
            src = attrs_dict.get('src', '')
            alt = attrs_dict.get('alt', '')
            if 'why-the-riser' in src or 'riser' in src.lower() or 'for-who' in src.lower() or 'techspecs' in src.lower() or 'ourclubs' in src.lower():
                print(f"IMG ASSET: {src} (alt={alt})")
        elif tag == 'source':
            srcset = attrs_dict.get('srcset', '')
            media = attrs_dict.get('media', '')
            if 'riser' in srcset.lower() or 'who' in srcset.lower():
                print(f"SOURCE ASSET: srcset={srcset} (media={media})")
                
        # Capture spec details
        if tag == 'div' and ('spec' in attrs_dict.get('class', '') or 'techspec' in attrs_dict.get('class', '')):
            self.in_specs = True
            
        # Capture intro
        if tag == 'section' and 'intro' in attrs_dict.get('class', ''):
            self.in_intro = True

    def handle_endtag(self, tag):
        if self.tags_stack:
            self.tags_stack.pop()
        if tag == 'div' and self.in_specs:
            self.in_specs = False
        if tag == 'section' and self.in_intro:
            self.in_intro = False

    def handle_data(self, data):
        data_clean = data.strip()
        if not data_clean:
            return
            
        if self.in_intro:
            self.intro_text.append(data_clean)
        elif self.in_specs:
            print(f"SPEC PIECE: {data_clean}")
            
        # Look for general Riser texts like tab content
        # We can print any short paragraphs containing Riser or details
        if len(data_clean) > 5 and ('riser' in data_clean.lower() or 'control' in data_clean.lower() or 'precision' in data_clean.lower() or 'forgiving' in data_clean.lower()):
            # Let's print out text pieces
            parent_tag, parent_attrs = self.tags_stack[-1] if self.tags_stack else (None, {})
            p_class = parent_attrs.get('class', '')
            print(f"TEXT PIECE (parent={parent_tag}, class={p_class}): {data_clean}")

def fetch_and_extract(url, lang_name):
    print(f"\n--- EXTRACTING {lang_name} CONTENT ---")
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req) as response:
            html = response.read().decode('utf-8')
        extractor = DataExtractor()
        extractor.feed(html)
        if extractor.intro_text:
            print(f"INTRO TEXTS: {' | '.join(extractor.intro_text)}")
    except Exception as e:
        print(f"Error: {e}")

fetch_and_extract("https://golfyr.com/sevenclubgame/the-riser/?v=d88fc6edf21e", "ENGLISH")
fetch_and_extract("https://golfyr.com/de/sevenclubgame/the-riser/", "GERMAN")
