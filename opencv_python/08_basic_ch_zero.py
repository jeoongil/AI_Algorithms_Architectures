import cv2
import numpy as np

src = cv2.imread("tomato.jpg",cv2.IMREAD_COLOR)

height, width, channel = src.shape

b = src[:, :, 0]
g = src[:, :, 1]

zero = np.zeros((height, width, 1), dtype=np.uint8)

bgz = cv2.merge((b, g, zero))

cv2.imshow("Blue+Green+Zero", bgz)

cv2.waitKey()
cv2.destroyAllWindows()


