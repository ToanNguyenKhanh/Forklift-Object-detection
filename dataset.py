import os
import cv2
import json
import glob
import shutil

if __name__ == '__main__':
    root = 'forklift_coco/valid'
    global_width = 640
    global_height = 640
    output_dir = 'forklift_yolo'

    if os.path.isdir(output_dir):
        shutil.rmtree(output_dir)
    os.makedirs(output_dir)

    os.makedirs(os.path.join(output_dir, 'images', 'train'))
    os.makedirs(os.path.join(output_dir, 'images', 'val'))
    os.makedirs(os.path.join(output_dir, 'labels', 'train'))
    os.makedirs(os.path.join(output_dir, 'labels', 'val'))

    json_file = list(glob.iglob("{}/*.json".format(root)))
    print(json_file)
    images_name = []
    for img_name in os.listdir(root):
        if img_name.endswith('jpg'):
            images_name.append(img_name)

    with open(json_file[0], 'r') as json_file:
        data = json.load(json_file)
        images_json = data['images']
        annotations = data['annotations']

    count = 1
    bbox_list = []

    for image in images_name:
        image_path = os.path.join(root, image)
        read_image = cv2.imread(image_path)
        cv2.imwrite(os.path.join(output_dir, 'images', 'val', '{}.jpg'.format(count)), read_image)

        current_bboxes = []
        for obj in images_json:
            if image == obj['file_name']:
                image_id = obj['id']
                for annotation in annotations:
                    if annotation['image_id'] == image_id:
                        bbox = annotation['bbox']
                        category_id = annotation['category_id']
                        current_bboxes.append([bbox, category_id])

        with open(os.path.join(output_dir, 'labels', 'val', '{}.txt'.format(count)), 'w') as text_file:
            for box in current_bboxes:
                (xmin, ymin, width, height), cat = box
                xcent = (xmin + width / 2) / global_width
                ycent = (ymin + height / 2) / global_height
                width /= global_width
                height /= global_height
                text_file.write("{} {:.6f} {:.6f} {:.6f} {:.6f}\n".format(cat, xcent, ycent, width, height))

        count += 1
        print(count)
