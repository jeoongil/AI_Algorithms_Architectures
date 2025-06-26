import cv2

topLeft = (50,50)
bold = 0

# Callback function for the trackbar
def on_bold_trackbar(value):
    global bold
    bold = value

cap = cv2.VideoCapture(0)
cv2.namedWindow ("Camera")
cv2.createTrackbar("bold", "Camera", bold, 10, on_bold_trackbar)

# 성공적으로 video device가 열렸으면 while문 반복
while(cap.isOpened()):
    # 한 프레임을 읽어옴
    ret, frame = cap.read()
    if ret is False:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    
    # Text
    cv2.putText(frame, "Text", topLeft, cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 255), 1 + bold)
    
    # Display
    cv2.imshow("Camera",frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
    
