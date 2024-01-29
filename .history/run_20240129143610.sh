#!/bin/bash
# 激活conda环境（替换为你的环境名）
#source ~/anaconda3/etc/profile.d/conda.sh
conda activate pixtext

# 运行Python程序 (GUI)
python /path/to/main.py

# 执行截图
flameshot gui -p /home/knight/迅雷下载/pix2text/image

# 获取最新的截图文件
LATEST_IMAGE=$(ls -Art /home/knight/迅雷下载/pix2text/image | tail -n 1)
IMAGE_PATH="/home/knight/迅雷下载/pix2text/image/$LATEST_IMAGE"

# 执行识别
python /home/knight/迅雷/pix2.py "$IMAGE_PATH" /home/knight/迅雷下载/pix2text/text
