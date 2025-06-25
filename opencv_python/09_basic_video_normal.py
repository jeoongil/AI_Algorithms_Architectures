import numpy as np
import cv2

cap = cv2.VideoCapture("son.mp4")

while(cap.isOpened()):
    ret, frame = cap.read()

    if ret is False:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    
    cv2.imshow("Frame",frame)

    key = cv2.waitKey(30)
    if key & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
