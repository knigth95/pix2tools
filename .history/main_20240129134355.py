import os
import subprocess

import pyperclip as pc
from tkinter import Tk, Button, font

# 在导入pix2text前设置QT_PLUGIN_PATH环境变量
os.environ['QT_PLUGIN_PATH'] = '/home/knight/anaconda3/envs/pixtext/lib/python3.11/site-packages/cv2/qt/plugins'


class FormulaRecognizerApp:
    def __init__(self, master):
        self.master = master
        master.title("Formula Recognizer")

        # 设置窗口大小
        master.geometry("400x200")

        # 设置文件路径
        self.image_dir = '/home/knight/迅雷下载/pix2text/image'
        self.text_dir = '/home/knight/迅雷下载/pix2text/text'
        self.image_name = 'test.png'
        self.image_path = os.path.join(self.image_dir, self.image_name)
        self.text_path = os.path.join(self.text_dir, self.image_name.replace('.png', '.tex'))

        # 设置按钮样式
        btn_font = font.Font(size=12, weight='bold')

        # 截图按钮
        self.screenshot_btn = Button(master, text="Capture Screenshot", command=self.capture_screenshot, font=btn_font, height=2, width=20)
        self.screenshot_btn.pack(pady=10)

        # 识别按钮
        self.recognize_btn = Button(master, text="Recognize Formula", command=self.recognize_formula, font=btn_font, height=2, width=20)
        self.recognize_btn.pack(pady=10)

    def capture_screenshot(self):
        # 使用flameshot进行截图
        subprocess.run(['flameshot', 'gui', '-p', self.image_dir])

    def recognize_formula(self):
        # 使用Pix2Text识别图片中的公式
        p2t = Pix2Text(analyzer_config=dict(model_name='mfd'))
        outs = p2t.recognize(self.image_path)
        only_text = '\n'.join([out['text'] for out in outs])

        # 将结果保存到文本文件并复制到剪贴板
        with open(self.text_path, 'w') as file:
            file.write(only_text)
        pc.copy(only_text)

        # 显示通知
        os.system(f'notify-send "Pix2Text" "完成公式识别，已将公式写入剪贴板。" -i {self.image_path} -t 1000')

def main():
    root = Tk()
    app = FormulaRecognizerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
