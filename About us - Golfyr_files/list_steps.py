import os
import re

steps_dir = '/Users/sebastianlilliecreutz/.gemini/antigravity/brain/ddbfd671-0571-4cce-8510-9e1720ca57d2/.system_generated/steps'
if not os.path.exists(steps_dir):
    print("Steps dir does not exist!")
else:
    for step_num in sorted(os.listdir(steps_dir)):
        step_path = os.path.join(steps_dir, step_num)
        if not os.path.isdir(step_path):
            continue
        content_file = os.path.join(step_path, 'content.md')
        if os.path.exists(content_file):
            with open(content_file, 'r', encoding='utf-8') as f:
                head = f.read(1000)
            # Find any URL reference in the beginning of content.md
            url_match = re.search(r'(https?://[^\s\)]+)', head)
            url_str = url_match.group(1) if url_match else "No URL"
            print(f"Step {step_num}: URL = {url_str} ({os.path.getsize(content_file)} bytes)")
