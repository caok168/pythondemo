#  读取摄像头

import cv2

# cap = cv2.VideoCapture(0)  # 调用笔记本内置摄像头

cap = cv2.VideoCapture(0)

while 1:
    ret, frame = cap.read()
    cv2.imshow("cap", frame)
    if cv2.waitKey(100) & 0xff == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

