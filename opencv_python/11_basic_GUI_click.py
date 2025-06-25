import cv2

points = []

def draw_circle(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        points.append((x,y))

cap = cv2.VideoCapture(2)
cv2.namedWindow ("Camera")
cv2.setMouseCallback("Camera", draw_circle)

while(cap.isOpened()):
    ret, frame = cap.read()
    if not ret:
        break

    for pt in points:
        cv2.circle(frame, pt, 30, (255, 0, 0), 3)

    cv2.imshow("Camera",frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
    
