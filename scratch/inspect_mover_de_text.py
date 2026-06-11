import urllib.request

url_de = "https://golfyr.com/de/sevenclubgame/the-mover/"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

print("=== GERMAN SPECS ===")
req = urllib.request.Request(url_de, headers=headers)
try:
    with urllib.request.urlopen(req) as response:
        html = response.read().decode('utf-8')
    
    # search for Volume and the paragraph following it
    for line in html.split('\n'):
        if 'Volume' in line or '240' in line or 'volumen' in line or 'Volumen' in line:
            print(line.strip())
except Exception as e:
    print(f"Error: {e}")
