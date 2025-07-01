import numpy as np
import cv2
import os
import random

# 분할 비율
train_ratio = 0.8  # 80%는 train, 나머지는 validation

# 클래스 목록
classes = ['jelly_coke', 'jelly_green', 'jelly_orange']

# 저장 루트 디렉토리
base_dir = 'dataset_v2'
train_dir = os.path.join(base_dir, 'train')
val_dir = os.path.join(base_dir, 'validation')

# 클래스별 저장 번호 초기화
counter = {}

# 디렉토리 구조 생성 및 번호 초기화
for cls in classes:
    os.makedirs(os.path.join(train_dir, cls), exist_ok=True)
    os.makedirs(os.path.join(val_dir, cls), exist_ok=True)

    # 현재 폴더에 존재하는 파일 수 기반 번호 초기화
    train_files = [f for f in os.listdir(os.path.join(train_dir, cls)) if f.endswith('.jpg')]
    val_files = [f for f in os.listdir(os.path.join(val_dir, cls)) if f.endswith('.jpg')]
    counter[cls] = len(train_files) + len(val_files) + 1

# 웹캠 실행
cap = cv2.VideoCapture(0)
print(f"[AUTO SPLIT MODE] 실행 중: C → coke, G → green, O → orange, Q → 종료")

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    cv2.imshow("Haribo Capture", frame)
    key = cv2.waitKey(1) & 0xFF

    # 종료
    if key == ord('q'):
        break

    # 키 → 클래스 매핑
    elif key == ord('c'):
        label = 'jelly_coke'
    elif key == ord('g'):
        label = 'jelly_green'
    elif key == ord('o'):
        label = 'jelly_orange'
    else:
        continue  # 나머지 키는 무시

    # train or validation 폴더 선택
    if random.random() < train_ratio:
        split = 'train'
    else:
        split = 'validation'

    save_dir = os.path.join(base_dir, split, label)
    filename = f"{label}_{counter[label]:03d}.jpg"
    filepath = os.path.join(save_dir, filename)

    # 저장
    cv2.imwrite(filepath, frame)
    print(f"[{split.upper()}] Saved: {filepath}")
    counter[label] += 1

cap.release()
cv2.destroyAllWindows()

