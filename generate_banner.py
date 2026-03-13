import os
from PIL import Image, ImageDraw, ImageFont

def generate_banner():
    # YouTube recommended banner size
    width, height = 2560, 1440
    
    # Deep charcoal background color
    bg_color = (28, 30, 33)
    
    # Create the image
    img = Image.new('RGB', (width, height), color=bg_color)
    draw = ImageDraw.Draw(img)
    
    # Load the font
    try:
        # Use a high quality, clean sans-serif system font
        font = ImageFont.truetype("/usr/share/fonts/truetype/liberation2/LiberationSans-Bold.ttf", 90)
    except IOError:
        font = ImageFont.load_default()
        
    text1 = "PHYSICAL AI &"
    text2 = "CYBER-PHYSICAL SYSTEMS"
    
    # Calculate bounding boxes using newer textbbox method
    bbox1 = draw.textbbox((0, 0), text1, font=font)
    bbox2 = draw.textbbox((0, 0), text2, font=font)
    
    w1 = bbox1[2] - bbox1[0]
    h1 = bbox1[3] - bbox1[1]
    
    w2 = bbox2[2] - bbox2[0]
    h2 = bbox2[3] - bbox2[1]
    
    # Vertical spacing
    spacing = 40
    total_height = h1 + h2 + spacing
    
    # Centered X and Y coordinates
    x1 = (width - w1) / 2
    y1 = (height - total_height) / 2
    
    x2 = (width - w2) / 2
    y2 = y1 + h1 + spacing
    
    # Draw text
    text_color = (255, 255, 255)
    draw.text((x1, y1), text1, font=font, fill=text_color)
    draw.text((x2, y2), text2, font=font, fill=text_color)
    
    # Save the output
    out_path = '/home/caaren/dev/personal/camirian/final_youtube_banner_master_2560.png'
    img.save(out_path, quality=100)
    print(f"Successfully saved high-res banner to: {out_path}")
    
    # Check the size to ensure it's not somehow compressed
    statinfo = os.stat(out_path)
    print(f"File size confirmed: {statinfo.st_size} bytes")

if __name__ == "__main__":
    generate_banner()
