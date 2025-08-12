from PIL import Image

def image2key(image_path, size_w=8, size_h=8):
    img = Image.open(image_path).convert('L')
    img = img.resize((size_w, size_h), Image.Resampling.LANCZOS)

    pixels = list(img.getdata())
    pixels_4bit = [p // 16 for p in pixels]
    hex_string = ''.join(f'{p:x}' for p in pixels_4bit)
    return hex_string