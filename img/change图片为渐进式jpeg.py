from PIL import Image
from PIL import ImageFile

img_path = "p3.jpg"  # Make sure this path is correct
destination = "p3.jpeg"

try:
    with Image.open(img_path) as img:
        img.save(destination, "JPEG", quality=80, optimize=True, progressive=True)
except IOError:
    ImageFile.MAXBLOCK = img.size[0] * img.size[1]
    with Image.open(img_path) as img:
        img.save(destination, "JPEG", quality=80, optimize=True, progressive=True)