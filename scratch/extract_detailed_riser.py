import urllib.request
import re
from html.parser import HTMLParser

class RiserDetailExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.in_spec_name = False
        self.in_spec_val = False
        self.in_spec_desc = False
        self.in_why_title = False
        self.in_why_desc = False
        self.in_intro_headline = False
        self.in_intro_body = False
        self.in_who_title = False
        self.in_who_body = False
        
        self.current_tag_classes = []
        self.specs = []
        self.why_slides = []
        self.intro_head = ""
        self.intro_body = ""
        self.who_head = ""
        self.who_body = ""

    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)
        classes = attrs_dict.get('class', '').split()
        
        if 'techspec-name' in classes:
            self.in_spec_name = True
        elif 'techspec-value' in classes:
            self.in_spec_val = True
        elif tag == 'p' and self.current_is_in_spec_slide():
            self.in_spec_desc = True
            
        # For why slides
        if 'title' in classes and self.current_is_in_why_slide():
            self.in_why_title = True
        elif 'content' in classes and self.current_is_in_why_slide():
            self.in_why_desc = True
            
        # For intro
        if tag == 'h2' and 'intro-headline' in classes:
            self.in_intro_headline = True
        elif tag == 'p' and 'intro-body' in classes:
            self.in_intro_body = True
            
        # For who is it for
        if 'head' in classes:
            self.in_who_title = True
        elif 'additional-content' in classes:
            self.in_who_body = True

        self.current_tag_classes.append((tag, classes))

    def handle_endtag(self, tag):
        if self.current_tag_classes:
            self.current_tag_classes.pop()
        self.in_spec_name = False
        self.in_spec_val = False
        self.in_spec_desc = False
        self.in_why_title = False
        self.in_why_desc = False
        self.in_intro_headline = False
        self.in_intro_body = False
        self.in_who_title = False
        self.in_who_body = False

    def handle_data(self, data):
        data_clean = data.strip()
        if not data_clean:
            return
            
        if self.in_spec_name:
            self.specs.append({'name': data_clean, 'value': '', 'desc': ''})
        elif self.in_spec_val:
            if self.specs:
                self.specs[-1]['value'] = data_clean
        elif self.in_spec_desc:
            if self.specs:
                self.specs[-1]['desc'] = data_clean
                
        elif self.in_why_title:
            self.why_slides.append({'title': data_clean, 'desc': ''})
        elif self.in_why_desc:
            if self.why_slides:
                self.why_slides[-1]['desc'] = data_clean
                
        elif self.in_intro_headline:
            self.intro_head = data_clean
        elif self.in_intro_body:
            self.intro_body = data_clean
            
        elif self.in_who_title:
            self.who_head = data_clean
        elif self.in_who_body:
            self.who_body = data_clean

    def current_is_in_spec_slide(self):
        for tag, classes in self.current_tag_classes:
            if 'spec-slide' in classes:
                return True
        return False
        
    def current_is_in_why_slide(self):
        for tag, classes in self.current_tag_classes:
            if 'swiper-slide' in classes:
                # Check if we are inside simpleSliderTabNavContent
                pass
        return True # let's capture anyway

def run_extraction(url, lang):
    print(f"\n=================== {lang} ===================")
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req) as response:
            html = response.read().decode('utf-8')
        
        # Clean up some common WP structure spacing if needed
        parser = RiserDetailExtractor()
        parser.feed(html)
        
        print(f"Intro Headline: {parser.intro_head}")
        print(f"Intro Body: {parser.intro_body}")
        print("\nSpecs Found:")
        for spec in parser.specs:
            print(f"  - {spec['name']}: {spec['value']} | Desc: {spec['desc']}")
            
        print("\nWhy Slides Found:")
        for idx, slide in enumerate(parser.why_slides):
            print(f"  Slide {idx+1}: {slide['title']} | Desc: {slide['desc']}")
            
        print(f"\nWho is it for Headline: {parser.who_head}")
        print(f"Who is it for Body: {parser.who_body}")
        
    except Exception as e:
        print(f"Error: {e}")

run_extraction("https://golfyr.com/sevenclubgame/the-riser/?v=d88fc6edf21e", "ENGLISH")
run_extraction("https://golfyr.com/de/sevenclubgame/the-riser/", "GERMAN")
