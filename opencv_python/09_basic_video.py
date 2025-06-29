import numpy as np
import cv2

# Read from the recorded video file
cap = cv2.VideoCapture("son.mp4")

# 동영상 파일이 성공적으로 열렸으면 while문 반복
while(cap.isOpened()):
    # 한 프레임을 읽어옴
    ret, frame = cap.read()

    if ret is False:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    
    # Display
    cv2.imshow("Frame",frame)

    # 1ms 동안 대기하며 키 입력을 받고 'q' 입력 시 종료
    key = cv2.waitKey(1)
    if key & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
