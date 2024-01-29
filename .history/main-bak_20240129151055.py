# coding: utf-8

import os
import pyperclip as pc
from pix2text import Pix2Text

#识别图片所在路径及图片文件名
img_fp = '/home/knight/迅雷下载/pix2text/image/2024-01-29_13-33.png'
#初始化Pix2Text
p2t = Pix2Text(analyzer_config=dict(model_name='mfd'))
#识别图片
outs = p2t.recognize(img_fp)
# 如果只需要识别出的文字和Latex表示，可以使用下面行的代码合并所有结果
only_text = '\n'.join([out['text'] for out in outs])
#将识别结果复制到系统剪贴板
pc.copy(only_text)
#以Linux系统通知的形式告知公式识别完成
os.system('notify-send "Pix2Text" "完成公式识别，已将公式写入剪贴板。" -i /home/knight/迅雷下载/pix2text/crosshair.svg -t 1000 ')
