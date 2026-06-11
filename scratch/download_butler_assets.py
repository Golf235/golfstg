import os
import urllib.request

urls = {
    # Hero mobile image
    "260323_Marketing_Header_Images_09_498X1024-1-498x1024.jpg": "https://golfyr.com/wp-content/uploads/2026/03/260323_Marketing_Header_Images_09_498X1024-1-498x1024.jpg",
    
    # Why choose images
    "why-the-butler-2.jpg": "https://golfyr.com/wp-content/uploads/2025/07/why-the-butler-2.jpg",
    "why-the-butler-3.jpg": "https://golfyr.com/wp-content/uploads/2025/07/why-the-butler-3.jpg",
    
    # Tech specs
    "techspecs-butler-loft.png": "https://golfyr.com/wp-content/uploads/2025/07/techspecs-butler-loft.png",
    "techspecs-butler-swing-weight.png": "https://golfyr.com/wp-content/uploads/2025/09/techspecs-butler-swing-weight.png",
    "techspecs-butler-length.png": "https://golfyr.com/wp-content/uploads/2025/07/techspecs-butler-length.png",
    "techspecs-butler-lie.png": "https://golfyr.com/wp-content/uploads/2025/07/techspecs-butler-lie.png",
    
    # For who backgrounds
    "for-who-the-butler-1920.jpg": "https://golfyr.com/wp-content/uploads/2025/07/for-who-the-butler-1920.jpg",
    "for-who-the-butler-768-768x1024.jpg": "https://golfyr.com/wp-content/uploads/2025/07/for-who-the-butler-768-768x1024.jpg",
    "for-who-the-butler-430-498x1024.jpg": "https://golfyr.com/wp-content/uploads/2025/07/for-who-the-butler-430-498x1024.jpg",
}

output_dir = "/Users/sebastianlilliecreutz/Downloads/Home - Golfyr_files/The Butler - Golfyr_files"
os.makedirs(output_dir, exist_ok=True)

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

for filename, url in urls.items():
    dest = os.path.join(output_dir, filename)
    if os.path.exists(dest) and os.path.getsize(dest) > 0:
        print(f"{filename} already exists and is not empty. Skipping.")
        continue
    print(f"Downloading {url} -> {dest}...")
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req) as response:
            with open(dest, 'wb') as f:
                f.write(response.read())
        print(f"  Successfully downloaded {filename}")
    except Exception as e:
        print(f"  Error downloading {filename}: {e}")

print("All Butler downloads complete.")
