import subprocess
import os
import re
import json

about_path = '/Users/sebastianlilliecreutz/Downloads/Home - Golfyr_files/about.html'

with open(about_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Inject script before </body>
script = """
<script>
window.addEventListener('load', () => {
  setTimeout(() => {
    const data = {};
    const elements = {
      'slider_makers': '.simple-slider-makers',
      'simple_slider_makers': '.simpleSliderMakers',
      'swiper_wrapper': '.simple-slider-makers .swiper-wrapper',
      'swiper_slide': '.simple-slider-makers .swiper-slide',
      'image_wrapper': '.simple-slider-makers .swiper-slide .image-wrapper.d-none.d-xl-block',
      'img': '.simple-slider-makers .swiper-slide .image-wrapper.d-none.d-xl-block img'
    };
    for (const [key, selector] of Object.entries(elements)) {
      const el = document.querySelector(selector);
      if (el) {
        const rect = el.getBoundingClientRect();
        const computed = window.getComputedStyle(el);
        data[key] = {
          selector,
          width: rect.width,
          height: rect.height,
          display: computed.display,
          height_style: computed.height,
          min_height: computed.minHeight,
          max_height: computed.maxHeight,
          position: computed.position
        };
      } else {
        data[key] = null;
      }
    }
    const div = document.createElement('div');
    div.id = 'layout-debug-output';
    div.textContent = JSON.stringify(data);
    document.body.appendChild(div);
  }, 1000);
});
</script>
"""

html_with_debug = html.replace('</body>', script + '</body>')

temp_file = '/Users/sebastianlilliecreutz/Downloads/Home - Golfyr_files/temp_debug.html'
with open(temp_file, 'w', encoding='utf-8') as f:
    f.write(html_with_debug)

cmd = [
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "--headless",
    "--disable-gpu",
    "--window-size=1440,900",
    "--dump-dom",
    "--virtual-time-budget=5000",
    f"file://{temp_file}"
]

res = subprocess.run(cmd, capture_output=True, text=True)

if os.path.exists(temp_file):
    os.remove(temp_file)

match = re.search(r'<div id="layout-debug-output">(.*?)</div>', res.stdout)
if match:
    debug_data = json.loads(match.group(1))
    print(json.dumps(debug_data, indent=2))
else:
    print("Could not find debug output in dumped DOM!")
    print("Length of DOM:", len(res.stdout))
