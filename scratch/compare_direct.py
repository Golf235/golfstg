from PIL import Image, ImageChops, ImageStat

attached_path = "/Users/sebastianlilliecreutz/.gemini/antigravity/brain/633bc07e-1a63-423a-9de9-ae4a1302a620/media__1781191237520.png"
attached_img = Image.open(attached_path).convert('RGB')
attached_size = attached_img.size

files = [
    "/Users/sebastianlilliecreutz/.gemini/antigravity/brain/633bc07e-1a63-423a-9de9-ae4a1302a620/techspecs-opener-loft.png",
    "/Users/sebastianlilliecreutz/.gemini/antigravity/brain/633bc07e-1a63-423a-9de9-ae4a1302a620/techspecs-opener-lie.png",
    "/Users/sebastianlilliecreutz/.gemini/antigravity/brain/633bc07e-1a63-423a-9de9-ae4a1302a620/techspecs-opener-length.png",
    "/Users/sebastianlilliecreutz/.gemini/antigravity/brain/633bc07e-1a63-423a-9de9-ae4a1302a620/techspecs-opener-swing-weight.png"
]

for path in files:
    img = Image.open(path)
    if img.mode in ('RGBA', 'LA') or (img.mode == 'P' and 'transparency' in img.info):
        img = img.convert('RGBA')
        background = Image.new('RGBA', img.size, (255, 255, 255, 255))
        img = Image.alpha_composite(background, img)
    img_rgb = img.convert('RGB')
    img_resized = img_rgb.resize(attached_size, Image.Resampling.LANCZOS)
    
    diff = ImageChops.difference(attached_img, img_resized)
    stat = ImageStat.Stat(diff)
    diff_sum = sum(stat.sum)
    print(f"{path.split('/')[-1]}: Diff sum = {diff_sum:.2f}")
