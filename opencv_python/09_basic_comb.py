import numpy as np
import cv2
import os

cap = cv2.VideoCapture("son.mp4")

# 저장될 이미지 번호 초기화
frame_id = 1

while(cap.isOpened()):
    ret, frame = cap.read()
    
    if not ret:
      print("End of video, restarting...")
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
        continue
    # resize 영상
    frame_resized = cv2.resize(frame, (0,0), fx=0.5, fy=0.5)
    
    # 영상 출력
    cv2.imshow("Resized Frame", frame_resized)

    key = cv2.waitKey(30) # 적절한 재생 속도 설정
    if key & 0xFF == ord('q'):
        break
    elif key & 0xFF == ord('c'):
        # 프레임 이미지 저장
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
