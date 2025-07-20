#!/usr/bin/env python3
# scripts/image_convert_tiff_to_jpeg.py

from PIL import Image
import os

images_path = "../test_images/"

for file_name in os.listdir(images_path):
    # Process only the `.tiff` files
    if file_name.lower().endswith(".tiff"):
        print("Processing file:", file_name)
        with Image.open(os.path.join(images_path, file_name)) as image:
            # We now have an `Image` object `image`, we can process it
            # Convert the image to "RGB" mode
            image_rgb = image.convert("RGB")
            # Resize the image to 600 x 400
            image_rgb_resized = image_rgb.resize((600, 400))
            # Set the filepath for the new image
            output_filepath = os.path.join(
                images_path, file_name.replace(".tiff", ".jpeg")
            )
            # Save the modified image
            image_rgb_resized.save(output_filepath, "JPEG")
            print("Output file saved:", output_filepath)
