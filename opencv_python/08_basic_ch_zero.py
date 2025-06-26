import cv2
import numpy as np

src = cv2.imread("tomato.jpg",cv2.IMREAD_COLOR)

height, width, channel = src.shape

# Numpy 슬라이싱
b = src[:, :, 0]
g = src[:, :, 1]

# 빈 채널 생성 (모든 값이 0인 배열)
zero = np.zeros((height, width, 1), dtype=np.uint8)

# b, g, zero로 병합하여 blue-green 만 남기기
bgz = cv2.merge((b, g, zero))

cv2.imshow("Blue+Green+Zero", bgz)

cv2.waitKey()
cv2.destroyAllWindows()


