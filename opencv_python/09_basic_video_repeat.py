import numpy as np
import cv2

cap = cv2.VideoCapture("son.mp4")

while(cap.isOpened()):
    ret, frame = cap.read()

    if not ret:
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
        continue
    
    cv2.imshow("Looped Video",frame)

    key = cv2.waitKey(30)
    if key & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
