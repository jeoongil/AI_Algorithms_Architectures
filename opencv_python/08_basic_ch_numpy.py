import cv2
import numpy as np

src = cv2.imread("tomato.jpg",cv2.IMREAD_COLOR)

# Numpy 슬라이싱으로 채널 분리
b = src[:, :, 0] # Blue
g = src[:, :, 1] # Green
r = src[:, :, 2] # Red

cv2.imshow("Blue", b)
cv2.imshow("Green", g)
cv2.imshow("Red", r)
cv2.waitKey()
cv2.destroyAllWindows()


