import cv2
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array

# 모델과 클래스 로딩
model = load_model('/content/drive/MyDrive/best_model.h5')
class_names = ['jelly_coke', 'jelly_green', 'jelly_orange']  # 주의: 실제 학습된 class 순서와 일치해야 함

IMG_SIZE = 32

# 웹캠 캡처 시작
cap = cv2.VideoCapture(0)  # 0번 카메라

if not cap.isOpened():
    print("웹캠 열기 실패")
    exit()

print("웹캠 실행 중... 종료하려면 q 키 누르기")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # 중앙 영역 crop (32x32 크기, 예시: 중앙 100x100에서 resize)
    h, w, _ = frame.shape
    center_crop = frame[h//2-50:h//2+50, w//2-50:w//2+50]
    resized = cv2.resize(center_crop, (IMG_SIZE, IMG_SIZE))
    
    # 전처리
    image = resized.astype("float32") / 255.0
    image = np.expand_dims(image, axis=0)  # (1, 32, 32, 3)

    # 예측
    preds = model.predict(image, verbose=0)[0]  # shape: (3,)
    label_idx = np.argmax(preds)
    label_name = class_names[label_idx]
    confidence = preds[label_idx]

    # 확률 표시용 문자열 생성
    text = f"{label_name}: {confidence * 100:.2f}%"
    
    # 원본 영상에 결과 표시
    cv2.rectangle(frame, (w//2-50, h//2-50), (w//2+50, h//2+50), (0, 255, 0), 2)
    cv2.putText(frame, text, (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    # 화면 출력
    cv2.imshow("Haribo Classifier", frame)

    # 'q' 키 누르면 종료
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 정리
cap.release()
cv2.destroyAllWindows()

