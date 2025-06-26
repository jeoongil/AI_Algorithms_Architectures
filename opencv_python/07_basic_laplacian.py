import cv2

src = cv2.imread("Image.jpg", cv2.IMREAD_COLOR)
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

laplacian = cv2.Laplacian(gray, cv2.CV_64F) # 64F로 해야 음수도 표현 가능
laplacian = cv2.convertScaleAbs(laplacian) # 절댓값 및 8비트로 변환

cv2.imshow("Laplacian", laplacian)
cv2.waitKey()
cv2.destroyAllWindows()

