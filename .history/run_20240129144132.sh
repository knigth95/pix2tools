#!/bin/bash

# 激活conda环境（确保你的环境名是正确的）
conda activate pixtext

# 执行截图
flameshot gui -p /home/knight/迅雷下载/pix2text/image

# 等待用户完成截图，这里可以根据需要调整延时
sleep 5

# 获取最新的截图文件
LATEST_IMAGE=$(ls -Art /home/knight/迅雷下载/pix2text/image | tail -n 1)
IMAGE_PATH="/home/knight/迅雷下载/pix2text/image/$LATEST_IMAGE"

# 检查是否获取到了最新的图像文件
if [ -f "$IMAGE_PATH" ]; then
    # 执行识别
    python /home/knight/迅雷下载/pix2text/pix2.py "$IMAGE_PATH" /home/knight/迅雷下载/pix2text/text
else
    echo "No screenshot found."
fi
