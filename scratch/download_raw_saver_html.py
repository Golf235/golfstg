import urllib.request

def save_page(url, filename):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req) as response:
            html = response.read().decode('utf-8')
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"Saved {url} to {filename}")
    except Exception as e:
        print(f"Error saving {url}: {e}")

save_page("https://golfyr.com/sevenclubgame/the-saver/?v=d88fc6edf21e", "scratch/saver_en.html")
save_page("https://golfyr.com/de/sevenclubgame/the-saver/", "scratch/saver_de.html")
