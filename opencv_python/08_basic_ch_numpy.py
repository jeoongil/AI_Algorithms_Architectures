import cv2
import numpy as np

src = cv2.imread("tomato.jpg",cv2.IMREAD_COLOR)

b = src[:, :, 0]
g = src[:, :, 1]
r = src[:, :, 2]

cv2.imshow("Blue", b)
cv2.imshow("Green", g)
cv2.imshow("Red", r)
cv2.waitKey()
cv2.destroyAllWindows()


