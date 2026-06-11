import re
from html.parser import HTMLParser

class ButlerDetailExtractor(HTMLParser):
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
        
        self.in_where_title = False
        self.in_where_subtitle = False
        self.in_where_point = False
        
        self.current_tag_classes = []
        self.specs = []
        self.why_slides = []
        self.intro_head = ""
        self.intro_body = ""
        self.who_head = ""
        self.who_body = ""
        
        self.where_title = ""
        self.where_subtitle = ""
        self.where_points = []
        
        self.images = set()

    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)
        classes = attrs_dict.get('class', '').split()
        
        # Capture all images
        if tag == 'img' and 'src' in attrs_dict:
            self.images.add(attrs_dict['src'])
        if 'src' in attrs_dict:
            self.images.add(attrs_dict['src'])
        if 'data-src' in attrs_dict:
            self.images.add(attrs_dict['data-src'])
            
        if 'style' in attrs_dict:
            style = attrs_dict['style']
            urls = re.findall(r'url\((.*?)\)', style)
            for url in urls:
                url = url.strip('\'"')
                self.images.add(url)
        
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

        # For where section
        if 'where-headline' in classes or ('where' in classes and tag == 'h2'):
            self.in_where_title = True
        elif 'where-subtitle' in classes:
            self.in_where_subtitle = True
        elif 'where-point' in classes or tag == 'li':
            self.in_where_point = True

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
        self.in_where_title = False
        self.in_where_subtitle = False
        self.in_where_point = False

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

        elif self.in_where_title:
            self.where_title = data_clean
        elif self.in_where_subtitle:
            self.where_subtitle = data_clean
        elif self.in_where_point:
            self.where_points.append(data_clean)

    def current_is_in_spec_slide(self):
        for tag, classes in self.current_tag_classes:
            if 'spec-slide' in classes:
                return True
        return False
        
    def current_is_in_why_slide(self):
        return True

def run_local_extraction(filepath, lang):
    print(f"\n=================== {lang} ===================")
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()
    
    parser = ButlerDetailExtractor()
    parser.feed(html)
    
    print(f"Intro Headline: {parser.intro_head}")
    print(f"Intro Body: {parser.intro_body}")
    
    print("\nSpecs Found:")
    for spec in parser.specs:
        print(f"  - {spec['name']}: {spec['value']} | Desc: {spec['desc']}")
        
    print("\nWhy Slides Found:")
    why_filtered = [s for s in parser.why_slides if s['title'] or s['desc']]
    for idx, slide in enumerate(why_filtered):
        print(f"  Slide {idx+1}: {slide['title']} | Desc: {slide['desc']}")
        
    print(f"\nWhere Title: {parser.where_title}")
    print(f"Where Subtitle: {parser.where_subtitle}")
    print("Where Points:")
    for pt in parser.where_points:
        print(f"  - {pt}")

    print(f"\nWho is it for Headline: {parser.who_head}")
    print(f"Who is it for Body: {parser.who_body}")
    
    print("\nImage URLs Found:")
    for img in sorted(parser.images):
        if 'butler' in img.lower() or 'why' in img.lower() or 'spec' in img.lower():
            print(f"  {img}")

run_local_extraction("/Users/sebastianlilliecreutz/Downloads/Home - Golfyr_files/scratch/butler_en.html", "ENGLISH")
run_local_extraction("/Users/sebastianlilliecreutz/Downloads/Home - Golfyr_files/scratch/butler_de.html", "GERMAN")
