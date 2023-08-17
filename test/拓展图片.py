from PIL import Image

input_image_path = 'input.png'
output_image_path = 'output1.png'

# 打开输入图像
input_image = Image.open(input_image_path)

# 获取原始图像的宽度和高度
width, height = input_image.size

# 设置目标宽度
target_width = 2000

# 计算需要添加的黑色像素宽度
padding_width = target_width - width

# 创建一个新的图像，尺寸为目标宽度 x 原始高度
output_image = Image.new('RGB', (target_width, height), (0, 0, 0))

# 将原始图像粘贴到新图像中间，左右留有相同数量的黑色像素填充
output_image.paste(input_image, (padding_width // 2, 0))

# 保存输出图像
output_image.save(output_image_path)

print("图像处理完成并保存到", output_image_path)
