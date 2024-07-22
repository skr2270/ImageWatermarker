
# ImageWatermarker

ImageWatermarker is a script that adds a watermark to all images in a specified input directory and saves the watermarked images to a specified output directory. It handles EXIF orientation to ensure images are correctly rotated and maintains image quality.

## Requirements

- Python 3.x
- Pillow library

## Installation

1. **Clone the repository or download the script file.**

2. **Install the required library:**

   ```bash
   pip install pillow
   ```

3. **Ensure the font file `Maharlika-Regular.ttf` is in the same directory as the script.**

## Usage

1. **Open the script file (`watermark_multiple_images.py`) in a text editor.**

2. **Set the paths to the input and output directories and the watermark text in the `main()` function:**

   ```python
   input_directory = "G:/My Drive/THC/Person"
   output_directory = "G:/My Drive/THC/Watermarked Person"
   watermark_text = "The Horizon Collections"
   ```

3. **Run the script:**

   ```bash
   python watermark_multiple_images.py
   ```

## Script Details

The script processes each image in the input directory, adds a centered watermark with the specified text, and saves the watermarked image to the output directory. It handles EXIF orientation to ensure images are correctly rotated and maintains the original image quality.

### Script Structure

- **add_watermark(image_path, output_path, watermark_text, font_size=150, opacity=200):**
  - Adds a watermark to a single image and saves it.
  - Handles EXIF orientation to ensure the image is correctly rotated.
  - Maintains the original image quality.

- **main():**
  - Sets the input and output directories and the watermark text.
  - Iterates through all images in the input directory and applies the watermark.

### Handling EXIF Orientation

The script reads the EXIF data of each image to determine its orientation. It rotates the image accordingly and then resets the EXIF orientation tag to ensure the image is displayed correctly in all viewers.

### Example

```python
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
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

If you have suggestions for improvements, feel free to submit a pull request or open an issue.

## Acknowledgements

This script uses the [Pillow](https://python-pillow.org/) library for image processing.
