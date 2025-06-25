import cv2
from PIL import ImageFont, ImageDraw, Image
import numpy as np

topLeft = (50,200)
bold = 1
font_scale = 1.0
r, g, b = 255, 255, 255

fontpath = "/usr/share/fonts/truetype/nanum/NanumGothic.ttf"

def on_bold_trackbar(value):
    global bold
    bold = max(value, 1)

def on_fontscale_trackbar(value):
    global font_scale
    font_scale = max(value / 10.0, 0.1)

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
cv2.createTrackbar("Bold", "Camera", bold, 10, on_bold_trackbar)
cv2.createTrackbar("FontSize", "Camera", int(font_scale * 10), 50,  on_fontscale_trackbar)
cv2.createTrackbar("R", "Camera", r, 255, on_r)
cv2.createTrackbar("G", "Camera", g, 255, on_g)
cv2.createTrackbar("B", "Camera", b, 255, on_b)

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret is False:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    
    font = ImageFont.truetype(fontpath, int(font_scale * 30))

    frame_pil =  Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    draw = ImageDraw.Draw(frame_pil)

    text = "안녕하세요, jeoongil!"
    for dx in range(-bold +1, bold):
        for dy in range(-bold +1, bold):
            draw.text((topLeft[0] + dx, topLeft[1] +dy), text, font=font, fill=(r, g, b))

    frame = cv2.cvtColor(np.array(frame_pil), cv2.COLOR_RGB2BGR)

    cv2.imshow("Camera",frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
    
