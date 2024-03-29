"""
@author: <nktoan163@gmail.com>
"""
import cv2
import json

file_name = '0VE1OCAVLKMX_jpg.rf.7e7d3d800877fb2cc60c249371f38dcc.jpg'
image = cv2.imread('forklift_coco/train/{}'.format(file_name))

annotation_file_path = 'forklift_coco/train/_annotations.coco.json'
with open(annotation_file_path, "r") as json_file:
    json_data = json.load(json_file)
    annotations = json_data['annotations']
    category = json_data['categories']

for annotation in annotations:
    image_id = annotation['image_id']
    print("image_id:", image_id)

image_id = None
for img in json_data['images']:
    if img['file_name'] == file_name:
        image_id = img['id']
        break

if image_id is not None:
    for ann in annotations:
        if ann['image_id'] == image_id:
            bbox = ann['bbox']
            xmin, ymin, width, height = map(int, bbox)
            cv2.rectangle(image, (xmin, ymin), (xmin + width, ymin + height), (0, 255, 0), 2)

cv2.imshow('Image with Bounding Boxes', image)
cv2.waitKey(0)

