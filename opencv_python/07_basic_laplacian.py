import cv2

src = cv2.imread("Image.jpg", cv2.IMREAD_COLOR)
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

laplacian = cv2.Laplacian(gray, cv2.CV_64F)
laplacian = cv2.convertScaleAbs(laplacian)

cv2.imshow("Laplacian", laplacian)
cv2.waitKey()
cv2.destroyAllWindows()

