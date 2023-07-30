import os
from PIL import Image

def batch_convert_to_progressive_jpeg(source_folder, destination_folder):
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    for filename in os.listdir(source_folder):
        if filename.lower().endswith(".jpg"):
            source_path = os.path.join(source_folder, filename)
            destination_path = os.path.join(destination_folder, filename)

            # Open the image and convert it to progressive JPEG
            with Image.open(source_path) as img:
                # Save the image as a progressive JPEG
                img.save(destination_path, "JPEG", quality=100, progressive=True)

            # Remove the original non-progressive JPEG
            os.remove(source_path)

if __name__ == "__main__":
    source_folder = "."
    destination_folder = os.path.join(source_folder, "lese")

    batch_convert_to_progressive_jpeg(source_folder, destination_folder)
