# main.py
from tkinter import Tk, Button, font

class FormulaRecognizerApp:
    def __init__(self, master):
        self.master = master
        master.title("Formula Recognizer")

        # 设置窗口大小
        master.geometry("400x200")

        # 设置按钮样式
        btn_font = font.Font(size=12, weight='bold')

        # 截图按钮
        self.screenshot_btn = Button(master, text="Capture Screenshot", command=self.capture_screenshot, font=btn_font, height=2, width=20)
        self.screenshot_btn.pack(pady=10)

        # 识别按钮
        self.recognize_btn = Button(master, text="Recognize Formula", command=self.recognize_formula, font=btn_font, height=2, width=20)
        self.recognize_btn.pack(pady=10)

    def capture_screenshot(self):
        # 执行截图脚本
        print("Capture Screenshot button clicked")

    def recognize_formula(self):
        # 执行识别脚本
        print("Recognize Formula button clicked")

def main():
    root = Tk()
    app = FormulaRecognizerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
