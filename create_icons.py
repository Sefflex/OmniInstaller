from PIL import Image, ImageDraw, ImageFont
import os

APPS = {
    "chrome": ("#4285F4", "C"),
    "firefox": ("#FF9500", "F"),
    "vlc": ("#FF5722", "V"),
    "spotify": ("#1DB954", "S"),
    "steam": ("#171A21", "St"),
    "discord": ("#5865F2", "D"),
    "vscode": ("#007ACC", "VS"),
    "7zip": ("#000000", "7z"),
    "python": ("#3776AB", "Py")
}

def create_icon(name, color, text):
    size = (64, 64)
    img = Image.new('RGBA', size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Yuvarlak arka plan
    draw.ellipse([2, 2, 62, 62], fill=color)
    
    # Metin (Basit bir font kullanmaya çalış, yoksa default)
    try:
        font = ImageFont.truetype("arial.ttf", 24)
    except:
        font = ImageFont.load_default()
        
  
    draw.text((20, 15), text, fill="white", font=font)
    
    path = os.path.join("assets", f"{name}.png")
    img.save(path)
    print(f"Created: {path}")

if __name__ == "__main__":
    if not os.path.exists("assets"):
        os.makedirs("assets")
        
    for name, (color, text) in APPS.items():
        create_icon(name, color, text)

