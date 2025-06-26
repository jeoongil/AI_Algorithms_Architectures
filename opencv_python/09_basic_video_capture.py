import numpy as np
import cv2
import os

cap = cv2.VideoCapture("son.mp4")
frame_id = 1 # 저장할 이미지 번호

while(cap.isOpened()):
    ret, frame = cap.read()
    if not ret:
        break
    
    cv2.imshow("Frame Capture",frame)

    key = cv2.waitKey(30)
    if key & 0xFF == ord('q'):
        break
    elif key & 0xFF == ord('c'):
        # 중복 방지 : 존재하지 않는 번호 찾기
        while True:
            filename = f"{frame_id:03d}.jpg"
            if not os.path.exists(filename):
                break
            frame_id += 1
        cv2.imwrite(filename, frame)
        print(f"Saved frame as {filename}")
        frame_id += 1

cap.release()
cv2.destroyAllWindows()
