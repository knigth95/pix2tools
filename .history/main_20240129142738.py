from tkinter import Tk, Button, font
import flameshot
import pix2

class FormulaRecognizerApp:
    def __init__(self, master):
        self.master = master
        master.title("Formula Recognizer")

        # 设置窗口大小
        master.geometry("400x200")

        # 设置文件路径
        self.image_dir = '/home/knight/迅雷下载/pix2text/image'
        self.text_dir = '/home/knight/迅雷下载/pix2text/text'

        # 设置按钮样式
        btn_font = font.Font(size=12, weight='bold')

        # 截图按钮
        self.screenshot_btn = Button(master, text="Capture Screenshot", command=self.capture_screenshot, font=btn_font, height=2, width=20)
        self.screenshot_btn.pack(pady=10)

        # 识别按钮
        self.recognize_btn = Button(master, text="Recognize Formula", command=self.recognize_formula, font=btn_font, height=2, width=20)
        self.recognize_btn.pack(pady=10)

    def capture_screenshot(self):
        flameshot.capture_screenshot(self.image_dir)
        self.image_path = flameshot.get_latest_image(self.image_dir)

    def recognize_formula(self):
        if self.image_path:
            pix2.recognize_formula(self.image_path, self.text_dir)

def main():
    root = Tk()
    app = FormulaRecognizerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
