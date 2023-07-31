from PIL import Image # pip3 install pillow
 
origin_file_path = './origin.jpeg'
progressive_file_path = './progressive.jpeg'
 
original_image = Image.open(origin_file_path)
original_image.convert('RGB')
original_image.save(progressive_file_path, optimize=True, quality=100, progressive=True)