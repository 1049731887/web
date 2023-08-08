from PIL import Image
import os


def is_progressive_jpeg(image_path):
    try:
        with Image.open(image_path) as img:
            return "progressive" in img.info and img.info["progressive"]
    except IOError:
        return False


if __name__ == "__main__":
    image_name = input("请输入图片名（包括文件扩展名）：")
    image_path = os.path.join(".", image_name)

    if is_progressive_jpeg(image_path):
        print("这是渐进式JPEG图片。")
    else:
        print("这不是渐进式JPEG图片。")
