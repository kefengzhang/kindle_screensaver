import os
import sys
import random
from PIL import Image
from datetime import datetime

def resize_images(width=1272, height=1696):
    """
    调整目录下所有图片的尺寸并重命名，确保另一条边超出目标尺寸，然后进行切割。
    """

    # 创建按时间命名的目录
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_dir = f"resized_images_{timestamp}"
    os.makedirs(output_dir, exist_ok=True)

    i = 0  # 初始化索引

    # 获取所有图片文件并随机排序
    image_files = [f for f in os.listdir('.') if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]
    random.shuffle(image_files)

    for filename in image_files:
        try:
            img = Image.open(filename)
            original_width, original_height = img.size

            # 如果原始尺寸与目标尺寸一致，则只修改文件名
            if original_width == width and original_height == height:
                new_filename = f"bg_ss{i:02d}.png"
                new_filepath = os.path.join(output_dir, new_filename)
                img.save(new_filepath, 'PNG', quality=20)
                print(f"已处理：{filename} -> {new_filepath}")
                i += 1
                continue

            # 计算缩放比例，确保另一条边超出目标尺寸
            if original_width / width > original_height / height:
                width_ratio = width / original_width
                new_height = int(original_height * width_ratio)
                img = img.resize((width, new_height), Image.LANCZOS)
                if new_height < height:
                    height_ratio = height / original_height
                    new_width = int(original_width * height_ratio)
                    img = img.resize((new_width, height), Image.LANCZOS)
            else:
                height_ratio = height / original_height
                new_width = int(original_width * height_ratio)
                img = img.resize((new_width, height), Image.LANCZOS)
                if new_width < width:
                    width_ratio = width / original_width
                    new_height = int(original_height * width_ratio)
                    img = img.resize((width, new_height), Image.LANCZOS)

            # 计算裁剪区域
            left = (img.size[0] - width) // 2
            top = (img.size[1] - height) // 2

            # 从中心裁剪图片
            img = img.crop((left, top, left + width, top + height))

            # 转换为黑白并降低图片质量
            img = img.convert('L')

            # 将图片保存为PNG格式并重命名
            new_filename = f"bg_ss{i:02d}.png"
            new_filepath = os.path.join(output_dir, new_filename)
            img.save(new_filepath, 'PNG', quality=20)
            print(f"已处理：{filename} -> {new_filepath}")
            i += 1

        except Exception as e:
            print(f"处理 {filename} 时出错：{e}")

if __name__ == "__main__":
    if len(sys.argv) == 1:
        resize_images()
    elif len(sys.argv) == 3:
        try:
            width = int(sys.argv[1])
            height = int(sys.argv[2])
            resize_images(width, height)
        except ValueError:
            print("宽度和高度必须是整数。")
            sys.exit(1)
    else:
        print("用法：python script.py [宽度] [高度]")
        sys.exit(1)