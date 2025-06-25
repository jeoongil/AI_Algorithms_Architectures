import numpy as np
import cv2

cap = cv2.VideoCapture("son.mp4")

while(cap.isOpened()):
    ret, frame = cap.read()
    if not ret:
        break

    resized_frame = cv2.resize(frame, (0,0), fx=0.5, fy=0.5)
    
    cv2.imshow("Resized Viedo", resized_frame)

    key = cv2.waitKey(30)
    if key & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
