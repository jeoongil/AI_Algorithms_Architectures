import cv2

src = cv2.imread("my_input.jpg",cv2.IMREAD_COLOR)
dst = cv2.blur(src, (21,21), anchor=(-1,1), borderType=cv2.BORDER_DEFAULT)

cv2.imshow("dst", dst)
cv2.waitKey()
cv2.destroyAllWindows()
