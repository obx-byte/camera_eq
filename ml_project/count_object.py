import os ,shutil,random
from ultralytics import YOLO
import supervision as sv
import cv2 as cv





#capture The Image From The camera 

# folder_path = r"C:\Users\v.hariharasudhan\Desktop\ML Task\ml_project\archive\Full  Water level\Full  Water level"
# files = os.listdir(folder_path)
# image_files = [f for f in files if f.endswith((".jpg", ".png"))]

# for file_name in image_files:
#     image_path = os.path.join(folder_path, file_name)
#     image = cv.imread(image_path)
    
#     if image is None:
#         print(f"Failed to load {file_name}")
#         continue

   
  
#     cv.imshow(file_name, image)
    

#     key = cv.waitKey(0)
#     if key == 27:  
#         break

# cv.destroyAllWindows()




# train the model about the ml learning 


#load the models
# model=YOLO("yolov8s.pt")

# IMAGE_FOlDER="images"
# LABEL_FOLDER="labels"
# os.makedirs(LABEL_FOLDER,exist_ok=True)

# for img_name in os.listdir(IMAGE_FOlDER):
#     img_path=os.path.join(IMAGE_FOlDER,img_name)
#     result =model(img_path)
#     detections=sv.Detections.from_ultralytics(result[0])
#     label_path=os.path.join(LABEL_FOLDER,img_name.replace(".jpg",".txt"))
#     sv.YOlO







model = YOLO("yolov8s.pt")

print(model())

IMAGE_FOLDER = "dataset/images"
LABEL_FOLDER = "dataset/labels"
os.makedirs(LABEL_FOLDER, exist_ok=True)

for img_name in os.listdir(IMAGE_FOLDER):
    img_path = os.path.join(IMAGE_FOLDER, img_name)

    results = model(img_path)[0]

    detections = sv.Detections.from_ultralytics(results)

    width, height = results.orig_shape[1], results.orig_shape[0]

    txt_name = img_name.rsplit(".", 1)[0] + ".txt"
    label_path = os.path.join(LABEL_FOLDER, txt_name)

    with open(label_path, "w") as f:
        for box, cls in zip(detections.xyxy, detections.class_id):
            x1, y1, x2, y2 = box

            # Convert to YOLO-format (normalized)
            x_center = ((x1 + x2) / 2) / width
            y_center = ((y1 + y2) / 2) / height
            w = (x2 - x1) / width
            h = (y2 - y1) / height

            f.write(f"{cls} {x_center} {y_center} {w} {h}\n")










# SRC_IMG = "dataset/images"
# SRC_LBL = "dataset/labels"
# DST = "dataset"

# IMG_EXTS = {".jpg", ".jpeg", ".png", ".bmp"}
# random.seed(42)

# train_img = os.path.join(DST, "images", "train")
# val_img   = os.path.join(DST, "images", "val")
# train_lbl = os.path.join(DST, "labels", "train")
# val_lbl   = os.path.join(DST, "labels", "val")

# for p in [train_img, val_img, train_lbl, val_lbl]:
#     os.makedirs(p, exist_ok=True)

# files = [f for f in os.listdir(SRC_IMG) if any(f.lower().endswith(ext) for ext in IMG_EXTS)]
# random.shuffle(files)
# split = int(len(files) * 0.8)
# train_files = files[:split]
# val_files = files[split:]

# def copy_list(file_list, img_dest, lbl_dest):
#     for fname in file_list:
#         src_img = os.path.join(SRC_IMG, fname)
#         src_lbl = os.path.join(SRC_LBL, fname.rsplit(".",1)[0] + ".txt")
#         dst_img = os.path.join(img_dest, fname)
#         dst_lbl = os.path.join(lbl_dest, fname.rsplit(".",1)[0] + ".txt")
#         shutil.copy2(src_img, dst_img)
#         if os.path.exists(src_lbl):
#             shutil.copy2(src_lbl, dst_lbl)

# copy_list(train_files, train_img, train_lbl)
# copy_list(val_files, val_img, val_lbl)

# print("Train:", len(train_files), "Val:", len(val_files))














