from ultralytics import YOLO
import supervision as sv
import os

IMAGE_FOLDER = "dataset/images"
LABEL_FOLDER = "dataset/labels"
TARGET_CLASS = "bottle"  
os.makedirs(LABEL_FOLDER, exist_ok=True)

model = YOLO("yolov8s.pt")
IMG_EXTS = {".jpg", ".jpeg", ".png"}

for img_name in os.listdir(IMAGE_FOLDER):
    if not any(img_name.lower().endswith(ext) for ext in IMG_EXTS):
       
        continue
    print(os.path.join(IMAGE_FOLDER,img_name))
    img_path = os.path.join(IMAGE_FOLDER, img_name)
    results = model(img_path)[0]
    detections = sv.Detections.from_ultralytics(results)

    names_map = results.names 

    width, height = results.orig_shape[1], results.orig_shape[0]

    txt_name = img_name.rsplit(".", 1)[0] + ".txt"
    label_path = os.path.join(LABEL_FOLDER, txt_name)

    with open(label_path, "w") as f:
        for (x1, y1, x2, y2), cls in zip(detections.xyxy, detections.class_id):
            cls_int = int(cls)

            cls_name = names_map.get(cls_int, str(cls_int)) if isinstance(names_map, dict) else names_map[cls_int]
            if cls_name != TARGET_CLASS:
                continue
            x_center = ((x1 + x2) / 2) / width
            y_center = ((y1 + y2) / 2) / height
            w = (x2 - x1) / width
            h = (y2 - y1) / height

            f.write(f"0 {x_center:.6f} {y_center:.6f} {w:.6f} {h:.6f}\n")

    print("Saved (filtered):", label_path)


