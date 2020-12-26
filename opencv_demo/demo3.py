import cv2


def cv_show(img, name):
    cv2.imshow(name, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


img = cv2.imread("imgs/1.png")
up = cv2.pyrUp(img)
cv_show(up, 'up')




