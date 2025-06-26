import cv2

# 텍스트 위치
topLeft = (50,200)

# 초기 폰트 크기
font_scale = 1

def on_fontscale_trackbar(value):
    global font_scale
    font_scale = max(value/10.0,0.1) # 최소값 0.1로 제한

cap = cv2.VideoCapture(0)
cv2.namedWindow ("Camera")
cv2.createTrackbar("FontSize", "Camera", int(font_scale*10), 50, on_fontscale_trackbar)

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret is False:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    cv2.putText(frame, "Text", topLeft, cv2.FONT_HERSHEY_SIMPLEX, font_scale, (0, 255, 255), 2)

    cv2.imshow("Camera",frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
    
