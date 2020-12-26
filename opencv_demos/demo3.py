import cv2
img = cv2.imread('imgs/1.png')

print(img.shape)
print(img.size)
print(img.dtype)

roi = img[100:200, 300:400]
img[50:150, 200:300] = roi
b = img[:, :, 0]

b, g, r = cv2.split(img)
img = cv2.merge((b, g, r))
cv2.imshow('roi', img)
cv2.waitKey(0)
