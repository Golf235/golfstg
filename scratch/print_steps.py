import json

log_path = "/Users/sebastianlilliecreutz/.gemini/antigravity/brain/633bc07e-1a63-423a-9de9-ae4a1302a620/.system_generated/logs/transcript.jsonl"
with open(log_path, 'r') as f:
    for line in f:
        data = json.loads(line)
        idx = data.get("step_index")
        if idx is not None and 378 <= idx <= 415:
            print(f"--- STEP {idx} ({data.get('source')}) ---")
            print(data.get("content"))
