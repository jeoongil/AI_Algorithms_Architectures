import cv2

topLeft = (50,200)
r, g, b = 255, 255, 255

def on_r (value):
    global r
    r = value

def on_g (value):
    global g
    g = value

def on_b (value):
    global b
    b = value

cap = cv2.VideoCapture(0)
cv2.namedWindow ("Camera")
cv2.createTrackbar("R", "Camera", r, 255, on_r)
cv2.createTrackbar("G", "Camera", g, 255, on_g)
cv2.createTrackbar("B", "Camera", b, 255, on_b)

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret is False:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    color = (b, g, r)
    cv2.putText(frame, "Text", topLeft, cv2.FONT_HERSHEY_SIMPLEX, 2, color, 2)

    cv2.imshow("Camera",frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
    
