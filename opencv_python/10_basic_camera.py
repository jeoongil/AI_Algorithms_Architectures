import numpy as np
import cv2

# Read from the first camera device, 외부 USB 카메라를 사용
cap = cv2.VideoCapture(2)

# 해상도 설정 
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
cap.set(cv2.CAP_PROP_FPS, 30)

# VideoWriter 설정 : output.mp4로 저장 (MP4V 코덱), 해상도 위와 같게 하기
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('output.mp4', fourcc, 30.0, (640, 480))

# 성공적으로 video device가 열렸으면 while문 반복(프레임 반복처리)
while(cap.isOpened()):
    # 한 프레임을 읽어옴
    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    
    # 영상 저장
    out.write(frame)

    # Display
    cv2.imshow("Camera",frame)
    
    # 1ms 동안 대기하며 키 입력을 받고 'q' 입력시 종료
    key = cv2.waitKey(1)
    if key & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()
