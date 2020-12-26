import cv2
img = cv2.imread("imgs/1.png")
print(img.shape)

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, img_threshold = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY)
ret, img_threshold2 = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY_INV)
cv2.imshow("img", img)
cv2.imshow("thre", img_threshold)
cv2.imshow("thre2", img_threshold2)

key = cv2.waitKey(0)
if key == 27:  # 按esc键时，关闭所有窗口
    print(key)
    cv2.destroyAllWindows()
cv2.imwrite("imgs/out.png", img_threshold)

