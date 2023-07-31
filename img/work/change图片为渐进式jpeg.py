import os
from PIL import Image

def batch_convert_to_progressive_jpeg(source_folder):
    lese_folder = os.path.join(source_folder, "lese")
    if not os.path.exists(lese_folder):
        os.makedirs(lese_folder)

    for filename in os.listdir(source_folder):
        if filename.lower().endswith(".jpg"):
            source_path = os.path.join(source_folder, filename)

            # Move the original image to "lese" folder
            os.rename(source_path, os.path.join(lese_folder, filename))

    for filename in os.listdir(lese_folder):
        if filename.lower().endswith(".jpg"):
            source_path = os.path.join(lese_folder, filename)
            destination_path = os.path.join(source_folder, filename)

            # Open the image and convert it to progressive JPEG
            with Image.open(source_path) as img:
                # Save the image as a progressive JPEG, overwriting the original
                img.save(destination_path, "JPEG", quality=100, progressive=True)

if __name__ == "__main__":
    source_folder = "."
    batch_convert_to_progressive_jpeg(source_folder)
