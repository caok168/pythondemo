import cv2
import matplotlib.pyplot as plt

img = cv2.imread('../imgs/1.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 简单滤波
ret, th1 = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
# Otsu滤波
ret2, th2 = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
print(ret2)
plt.figure()
plt.subplot(221), plt.imshow(gray, 'gray')
plt.subplot(222), plt.hist(gray.ravel(), 256)
plt.subplot(223), plt.imshow(th1, 'gray')
plt.subplot(224), plt.imshow(th2, 'gray')

plt.show()
