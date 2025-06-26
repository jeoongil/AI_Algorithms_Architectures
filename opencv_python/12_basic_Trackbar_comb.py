import cv2

# 초기 설정
topLeft = (50,200)
bold = 1
font_scale = 1.0
r, g, b = 255, 255, 255

# Callback function
def on_bold_trackbar(value):
    global bold
    bold = max(value, 1) # 최소 굵기 1

def on_fontscale_trackbar(value):
    global font_scale
    font_scale = max(value / 10.0, 0.1) # 최소 크기 0.1

def on_r (value):
    global r
    r = value

def on_g (value):
    global g
    g = value

def on_b (value):
    global b
    b = value

# 카메라 캡처 시작
cap = cv2.VideoCapture(0)

# 창과 트랙바 생성 
cv2.namedWindow ("Camera")
cv2.createTrackbar("Bold", "Camera", bold, 10, on_bold_trackbar)
cv2.createTrackbar("FontSize", "Camera", int(font_scale * 10), 50,  on_fontscale_trackbar)
cv2.createTrackbar("R", "Camera", r, 255, on_r)
cv2.createTrackbar("G", "Camera", g, 255, on_g)
cv2.createTrackbar("B", "Camera", b, 255, on_b)

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret is False:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    color = (b, g, r)
    
    # 텍스트 출력 
    cv2.putText(frame, "jeoongil", topLeft, cv2.FONT_HERSHEY_SIMPLEX, font_scale, color, bold)

    # 화면 출력
    cv2.imshow("Camera",frame)

    # 종료 조건
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
    
