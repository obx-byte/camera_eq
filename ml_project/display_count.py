import cv2
from ultralytics import YOLO
import os

""" Camera Ip Address """








model =YOLO("yolov8s.pt")

# ip_address="rstp://admin:Lgb@12345@192.168.54.177/"


model.train(data="dataset.yaml",epochs=50)


# img=cv2.imread(r"C:\Users\v.hariharasudhan\Desktop\ML Task\ml_project\assets\group-of-people-18.jpg")

# resize_img=cv2.resize(img,(500,400))

# count=0
# results=model(resize_img)[0]
# for box in results.boxes:

#     cls_id=int(box.cls[0])
#     print(cls_id)
#     cls_name=model.names[cls_id]
    
#     if cls_name=="person":
#         x1,y1,x2,y2=map(int ,box.xyxy[0])
#         cv2.rectangle(resize_img,(x1,y1),(x2,y2),(0,0,255),2)
#         cv2.putText(resize_img,"Person Detection",(x1, y1-10),
#                         cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,0), 4)
#         count+=1

#         cv2.imshow("Person Detection", resize_img)
#         cv2.waitKey(0)
#         cv2.destroyAllWindows()
# print("Count Bottle ",count)


