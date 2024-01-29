import os
import subprocess
from tkinter import Tk, Button
from pix2text import Pix2Text

class FormulaRecognizerApp:
    def __init__(self, master):
        self.master = master
        master.title("Formula Recognizer")

        # 设置文件路径
        self.image_dir = '/path/to/image/folder'
        self.text_dir = '/path/to/text/folder'
        self.image_path = os.path.join(self.image_dir, 'test.png')
        self.text_path = os.path.join(self.text_dir, 'test.txt')

        # 截图按钮
        self.screenshot_btn = Button(master, text="Capture Screenshot", command=self.capture_screenshot)
        self.screenshot_btn.pack()

        # 识别按钮
        self.recognize_btn = Button(master, text="Recognize Formula", command=self.recognize_formula)
        self.recognize_btn.pack()

    def capture_screenshot(self):
        # 使用flameshot进行截图
        subprocess.run(['flameshot', 'gui', '-p', self.image_dir])

    def recognize_formula(self):
        # 使用Pix2Text识别图片中的公式
        p2t = Pix2Text(analyzer_config=dict(model_name='mfd'))
        outs = p2t.recognize(self.image_path)
        only_text = '\n'.join([out['text'] for out in outs])

        # 将结果保存到文本文件
        with open(self.text_path, 'w') as file:
            file.write(only_text)

        # 可以在这里添加其他操作，比如复制到剪贴板或显示通知

def main():
    root = Tk()
    app = FormulaRecognizerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
