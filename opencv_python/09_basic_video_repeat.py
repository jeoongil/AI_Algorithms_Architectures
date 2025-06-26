import numpy as np
import cv2

cap = cv2.VideoCapture("son.mp4")

while(cap.isOpened()):
    ret, frame = cap.read()

    if not ret:
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0) # 프레임 위치를 처음으로 되감기
        continue
    
    cv2.imshow("Looped Video",frame)

    key = cv2.waitKey(30)
    if key & 0xFF == ord('q'): # 'q'를 누르게 되면 동영상 종료
        break

cap.release()
cv2.destroyAllWindows()
