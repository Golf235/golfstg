import urllib.request
import re
from html.parser import HTMLParser

class ImageParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)
        if tag == 'img':
            src = attrs_dict.get('src')
            data_src = attrs_dict.get('data-src')
            alt = attrs_dict.get('alt')
            print(f"img: src={src}, data-src={data_src}, alt={alt}")
        elif tag == 'source':
            srcset = attrs_dict.get('srcset')
            data_srcset = attrs_dict.get('data-srcset')
            print(f"source: srcset={srcset}, data-srcset={data_srcset}")
        
        style = attrs_dict.get('style')
        if style and 'url' in style:
            print(f"style: {style}")

url = "https://golfyr.com/sevenclubgame/the-mover/?v=d88fc6edf21e"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

req = urllib.request.Request(url, headers=headers)
try:
    with urllib.request.urlopen(req) as response:
        html = response.read().decode('utf-8')
        
    parser = ImageParser()
    parser.feed(html)
except Exception as e:
    print(f"Error fetching URL: {e}")
