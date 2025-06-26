import numpy as np
import cv2

# 이미지 파일을 Read 하고 Color space 정보 출력
color = cv2.imread("strawberry.jpg", cv2.IMREAD_COLOR)
print(color.shape)

height,width,channels = color.shape
cv2.imshow("Original Image",color)

cv2.waitKey(0)

# Color channel 을 B, G, R로 분할하여 출력
b,g,r = cv2. split(color)
rgb_split = np.concatenate((b,g,r),axis=1)
cv2.imshow("BGR Channels", rgb_split)

cv2.waitKey(0)

# 색공간을 BGR 에서 HSV로 변환
hsv = cv2.cvtColor(color, cv2.COLOR_BGR2HSV)

# Channel을 H, S, V 로 분할하여 출력
h,s,h = cv2.split(hsv)
hsv_split = np.comcatenate((h,s,v),axis=1)
cv2.imshow("Split HSV", hsv_split)

cv2.waitKey(0)
cv2.destroyAllWindows()
