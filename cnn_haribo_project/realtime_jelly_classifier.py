import cv2
import numpy as np
import tensorflow as tf
import os

# 모델 불러오기
model = tf.keras.models.load_model('final_model_1.h5')

# 클래스 이름 추출
class_names = sorted(os.listdir('dataset_v2/train'))  # 클래스 폴더명 기준

# 전처리 함수: 중앙 정사각형 crop + RGB 변환 + resize + 정규화
def preprocess_center_crop(frame, img_size=32):
    h, w, _ = frame.shape
    min_len = min(h, w)
    start_x = (w - min_len) // 2
    start_y = (h - min_len) // 2
    cropped = frame[start_y:start_y + min_len, start_x:start_x + min_len]
    
    rgb = cv2.cvtColor(cropped, cv2.COLOR_BGR2RGB)
    resized = cv2.resize(rgb, (img_size, img_size))
    normalized = resized.astype('float32') / 255.0
    return np.expand_dims(normalized, axis=0)  # (1, 64, 64, 3)

# 실시간 웹캠 실행
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    raise RuntimeError("웹캠을 열 수 없습니다.")

print("[INFO] 실시간 젤리 분류 시작... (종료: q)")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    input_img = preprocess_center_crop(frame)
    predictions = model.predict(input_img, verbose=0)[0]

    # 예측 결과 정렬
    sorted_indices = np.argsort(predictions)[::-1]

    for i, idx in enumerate(sorted_indices):
        class_name = class_names[idx]
        prob = predictions[idx] * 100
        text = f"{class_name} : {prob:.1f}%"
        color = (0, 255, 0) if i == 0 else (255, 255, 255)  # 최상위는 초록색
        cv2.putText(frame, text, (10, 30 + i * 30), cv2.FONT_HERSHEY_SIMPLEX,
                    0.9, color, 2)

    # 예측창 띄우기
    cv2.imshow("Jelly Classifier", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


