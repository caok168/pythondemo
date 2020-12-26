import cv2
img = cv2.imread('imgs/1.png')
pixel = img[100, 100]
img[100, 100] = [57, 63, 99]  # 设置像素值
b = img[100, 100, 0]  # 57,　获取(100, 100)处, blue通道像素值
g = img[100, 100, 1]  # 63
r = img[100, 100, 2]  # 68
r = img[100, 100, 2] = 99  # 设置red通道
# 获取和设置
piexl = img.item(100, 100, 2)
img.itemset((100, 100, 2), 99)

