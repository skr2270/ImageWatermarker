import os
from PIL import Image, ImageDraw, ImageFont, ExifTags

def add_watermark(image_path, output_path, watermark_text, font_size=150, opacity=200):
    # Load image
    image = Image.open(image_path)
    
    # Handle EXIF orientation
    try:
        for orientation in ExifTags.TAGS.keys():
            if ExifTags.TAGS[orientation] == 'Orientation':
                break
        exif = dict(image._getexif().items())
        
        if exif[orientation] == 3:
            image = image.rotate(180, expand=True)
        elif exif[orientation] == 6:
            image = image.rotate(270, expand=True)
        elif exif[orientation] == 8:
            image = image.rotate(90, expand=True)
        
        # Reset orientation tag
        exif[orientation] = 1
        image.info["exif"] = image._getexif().tobytes()
    except (AttributeError, KeyError, IndexError):
        # Cases: image doesn't have getexif
        pass

    # Make the image editable
    watermark = Image.new("RGBA", image.size)
    drawing = ImageDraw.Draw(watermark)
    
    # Define the font and size
    font_path = "Maharlika-Regular.ttf"  # Ensure the font file is in the same directory as the script
    font = ImageFont.truetype(font_path, font_size)
    
    # Calculate text size and position
    text_bbox = drawing.textbbox((0, 0), watermark_text, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]
    width, height = image.size
    x = (width - text_width) / 2
    y = (height - text_height) / 2

    # Add text to watermark
    drawing.text((x, y), watermark_text, fill=(255, 255, 255, opacity), font=font)

    # Combine watermark with image
    watermarked = Image.alpha_composite(image.convert("RGBA"), watermark)

    # Save watermarked image with high quality
    watermarked.convert("RGB").save(output_path, "JPEG", quality=100)

def main():
    # Paths to the input and output directories
    input_directory = "G:/My Drive/THC/Person"
    output_directory = "G:/My Drive/THC/Watermarked Person"
    os.makedirs(output_directory, exist_ok=True)
    
    # Set watermark text
    watermark_text = "The Horizon Collections"
    
    # Process each image in the input directory
    for filename in os.listdir(input_directory):
        if filename.lower().endswith(('png', 'jpg', 'jpeg', 'tiff', 'bmp', 'gif')):
            image_path = os.path.join(input_directory, filename)
            output_path = os.path.join(output_directory, filename)
            
            # Debugging
            print(f"Processing: {image_path}")
            
            add_watermark(image_path, output_path, watermark_text)
            print(f"Watermarked image saved as: {output_path}")

if __name__ == "__main__":
    main()
