import cv2

cap = cv2.VideoCapture(2)
topLeft = (50, 50)
bottomRight = (300, 300)

while(cap.isOpened()):
    ret, frame = cap.read()
    if not ret:
        break
    
    # 선
    cv2.line(frame, topLeft, bottomRight, (0, 255, 0), 5)
    
    # 사각형
    cv2.rectangle(frame, [pt+30 for pt in topLeft], [pt-30 for pt in bottomRight], (0, 0, 255), 5)

    # 텍스트 속성 변경
    font = cv2.FONT_HERSHEY_COMPLEX # 바뀐 글꼴
    text_position = (topLeft[0], bottomRight[1] + 50)

    cv2.putText(frame, 'OpenCV jeoongil', text_position, font, 1.5, (255, 0, 255), 3)

    cv2.imshow("Camera",frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
    
