from pix2text import Pix2Text
import pyperclip as pc
import os

def recognize_formula(image_path, text_dir):
    # 使用Pix2Text识别图片中的公式
    p2t = Pix2Text(analyzer_config=dict(model_name='mfd'))
    outs = p2t.recognize(image_path)
    only_text = '\n'.join([out['text'] for out in outs])

    text_path = os.path.join(text_dir, os.path.basename(image_path).replace('.png', '.tex'))

    # 将结果保存到文本文件并复制到剪贴板
    with open(text_path, 'w') as file:
        file.write(only_text)
    pc.copy(only_text)

    # 显示通知
    os.system(f'notify-send "Pix2Text" "完成公式识别，已将公式写入剪贴板。" -i {image_path} -t 1000')

    return text_path
