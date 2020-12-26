import cv2
import matplotlib.pyplot as plt

img2 = cv2.imread('imgs/1.png')
img = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
constant = cv2.copyMakeBorder(img, 20, 20, 20, 20, cv2.BORDER_CONSTANT, value=[0, 255, 0])
reflect = cv2.copyMakeBorder(img, 20, 20, 20, 20, cv2.BORDER_REFLECT)
reflect01 = cv2.copyMakeBorder(img, 20, 20, 20, 20, cv2.BORDER_REFLECT_101)
replicate = cv2.copyMakeBorder(img, 20, 20, 20, 20, cv2.BORDER_REPLICATE)
wrap = cv2.copyMakeBorder(img, 20, 20, 20, 20, cv2.BORDER_WRAP)
titles = ["constant", "reflect", "reflect01", "replicate", "wrap"]
images = [constant, reflect, reflect01, replicate, wrap]

for i in range(5):
    plt.subplot(2, 3, i+1)
    plt.imshow(images[i])
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])
plt.show()
