import cv2

# Read from the first camera device
cap = cv2.VideoCapture(2)

topLeft = (50, 50)
bottomRight = (300, 300)

# 성공적으로 video device가 열렸으면 while문 반복
while(cap.isOpened()):
    # 한 프레임을 읽어옴
    ret, frame = cap.read()
    
    # Line
    cv2.line(frame, topLeft, bottomRight, (0, 255, 0), 5)

    # Rectangle
    cv2.rectangle(frame, [pt+30 for pt in topLeft], [pt-30 for pt in bottomRight], (0, 0, 255), 5)

    # Text
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame, 'me', [pt+80 for pt in topLeft], font, 2, (0, 255, 255), 10)

    # Display
    cv2.imshow("Camera",frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
    
