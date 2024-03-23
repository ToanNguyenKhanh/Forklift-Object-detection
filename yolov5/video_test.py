import torch
import cv2

# Model
model = torch.hub.load("ultralytics/yolov5", "custom", path="runs/train/exp3/weights/best.pt")  # or yolov5n - yolov5x6, custom

# Images
cap = cv2.VideoCapture("test_forklift.mp4")
while cap.isOpened():
    flag, frame = cap.read()
    if not flag:
        break
    results = model(frame)
    print(results.pred, results.names, results)