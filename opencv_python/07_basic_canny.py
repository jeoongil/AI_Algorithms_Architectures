import cv2

src = cv2.imread("Image.jpg", cv2.IMREAD_COLOR)
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

edges = cv2.Canny(gray, threshold1=100, threshold2=200)

cv2.imshow("Canny Edge", edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
