from PIL import Image

def split_image(image, num_strips):
    width, height = image.size
    strip_width = width // num_strips
    strips = []
    
    for x in range(0, width, strip_width):
        box = (x, 0, x + strip_width, height)
        strip = image.crop(box)
        strips.append(strip)
    
    return strips

def rearrange_strips(strips, pattern):
    new_strips = [None] * len(strips)
    
    for i, index in enumerate(pattern):
        new_strips[i] = strips[index]
    
    return new_strips
def rearrange_strips(strips, pattern):
    new_strips = [None] * len(strips)
    
    for i, index in enumerate(pattern):
        if 0 <= index < len(strips):
            new_strips[i] = strips[index]
        else:
            print(f"Invalid index: {index}")
    
    return new_strips
def main(input_path, output_path, num_strips, pattern):
    image = Image.open(input_path)
    
    strips = split_image(image, num_strips)
    
    if len(strips) != num_strips:
        print("Error: Number of strips doesn't match.")
        return
    
    new_strips = rearrange_strips(strips, pattern)
    
    strip_width = strips[0].width
    new_image = Image.new('RGB', image.size)
    for i, strip in enumerate(new_strips):
        if strip is not None:
            x = i * strip_width
            new_image.paste(strip, (x, 0, x + strip_width, strip.height))
    
    new_image.save(output_path)
    print("New image saved as", output_path)

if __name__ == "__main__":
    input_path = "output1.png"  # 输入图片路径
    output_path = "output2.png"  # 输出图片路径
    num_strips = 400
    input_str = input("请输入一个表示数组的字符串：")
    pattern = eval(input_str)
    
    main(input_path, output_path, num_strips, pattern)
    input("按下 Enter 键继续...")