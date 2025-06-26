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

    # 텍스트
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame, 'jeoongil', [pt+50 for pt in topLeft], font, 2, (0, 255, 255), 10)

    # 동그라미 추가
    center = (200,200)
    radius = 40
    cv2.circle(frame, center, radius, (255, 255, 0), 5)

    cv2.imshow("Camera",frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
    
