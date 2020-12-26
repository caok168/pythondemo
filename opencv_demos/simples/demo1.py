import cv2
img = cv2.imread('../imgs/1.png', 1)
imgInfo = img.shape
print(imgInfo)

height = imgInfo[0]
width = imgInfo[1]
mode = imgInfo[2]

dstHeight = int(height*0.5)
dstWidth = int(width*0.5)
dst = cv2.resize(img, (dstWidth, dstHeight))
cv2.imshow('image', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
