import numpy as np
import cv2

cap = cv2.VideoCapture(2)


cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
cap.set(cv2.CAP_PROP_FPS, 30)

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('output.mp4', fourcc, 30.0, (640, 480))

while(cap.isOpened()):
    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    
    out.write(frame)
    cv2.imshow("Camera",frame)

    key = cv2.waitKey(1)
    if key & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()
