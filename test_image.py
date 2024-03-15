"""
@author: <nktoan163@gmail.com>
"""
import cv2
import numpy as np

image = cv2.imread('forklift_yolo/images/val/10.jpg')
height, width, _ = image.shape
with open('forklift_yolo/labels/val/10.txt', 'r') as text_file:
    data = text_file.readlines()
data = [line.strip().split() for line in data]
data = np.array(data, dtype=np.float32)
for bbox in data:
    print(bbox)
    _, xcent, ycent, w, h = bbox
    xcent *= width
    ycent *= height
    w *=width
    h *= height
    xmin = int(xcent - w / 2)
    ymin = int(ycent - h / 2)
    xmax = int(xcent + w / 2)
    ymax = int(ycent + h / 2)
    cv2.rectangle(image, (xmin, ymin), (xmax,ymax), (0, 255, 0), 2)
cv2.imshow('image', image)
cv2.waitKey(0)
