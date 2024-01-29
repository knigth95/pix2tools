import subprocess
import os

def capture_screenshot(image_dir):
    # 使用flameshot进行截图
    subprocess.run(['flameshot', 'gui', '-p', image_dir])

def get_latest_image(dir_path):
    # 获取指定目录下最新的 PNG 图片
    png_files = [os.path.join(dir_path, f) for f in os.listdir(dir_path) if f.endswith('.png')]
    if not png_files:
        return None
    latest_file = max(png_files, key=os.path.getmtime)
    return latest_file
