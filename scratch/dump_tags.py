import urllib.request
import re

url_en = "https://golfyr.com/sevenclubgame/the-riser/?v=d88fc6edf21e"
url_de = "https://golfyr.com/de/sevenclubgame/the-riser/"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

def print_clean_tags(url, label):
    print(f"\n=================== {label} HTML TAGS ===================")
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req) as response:
            html = response.read().decode('utf-8')
            
        # find all headings (h1, h2, h3, h4) and p elements inside a main or content container
        # We can extract anything between tag wrappers
        pattern = re.compile(r'<(h1|h2|h3|h4|p|div)[^>]*>(.*?)</\1>', re.DOTALL)
        for tag, content in pattern.findall(html):
            clean_content = re.sub(r'<[^>]*>', '', content).strip()
            # print if not empty and length is reasonable
            if clean_content and len(clean_content) < 500:
                # filter out navigation/footer text if possible
                if any(x in clean_content for x in ["Cookie", "PixelYourSite", "Facebook", "Google"]):
                    continue
                print(f"[{tag.upper()}]: {clean_content}")
    except Exception as e:
        print(f"Error: {e}")

print_clean_tags(url_en, "EN")
print_clean_tags(url_de, "DE")
