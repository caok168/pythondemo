# import cv2
#
# cap = cv2.VideoCapture("./Tennis1080p.h264")  # 打开视频
# while cap.isOpened():
#     ret, fram = cap.read()  # 读取视频返回视频是否结束的bool值和每一帧的图像
#     cv2.imshow('a', fram)
#     cv2.waitKey(1)
#     cv2.destroyAllWindows()

import cv2

cap = cv2.VideoCapture('./Tennis1080p.h264')

while(cap.isOpened()):
    ret, frame = cap.read()

    cv2.imshow('frame', frame)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

