import cv2
import numpy as np
import os


def test1():
    current_path = os.getcwd()
    img_path = current_path + "/imgs/1.png"
    img = cv2.imread(img_path)
    # cv2.imshow("11", img)
    # cv2.waitKey(0)
    print(img)
    print(img.shape)

    cv2.imwrite('imgs/test.jpg', img)


def test2():
    vc = cv2.VideoCapture('videos/test.mp4')
    if vc.isOpened():
        open, frame = vc.read()
    else:
        open = False

    while open:
        ret, frame = vc.read()
        if frame is None:
            break
        if ret == True:
            # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            cv2.imshow('result', frame)
            if cv2.waitKey(10) & 0xFF == 27:
                break

    vc.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    # test1()
    test2()
