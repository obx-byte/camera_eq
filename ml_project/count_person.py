import cv2
from ultralytics import YOLO


import tensorflow

model = YOLO("yolov8n.pt") 






def video_detection():

   
    ipaddress="rtsp://admin:Lgb@12345@192.168.54.177:554/"
    cap = cv2.VideoCapture(ipaddress)

    count = 0

    if not cap.isOpened():
        print(" Cannot open video stream")
        return

    while True:
        ret, frame = cap.read()

        if not ret:
            print(" Failed to read frame")
            break

        results = model(frame)

        for result in results:
            for box in result.boxes:
                cls_id = int(box.cls[0])
                cls_name = model.names[cls_id]

                if cls_name == "person":
                    x1, y1, x2, y2 = map(int, box.xyxy[0])
                    count += 1

                    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                    cv2.putText(frame, "Person", (x1, y1 - 10),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

        cv2.imshow("Person Detection YOLO", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        


        print(count)
    cap.release()
    cv2.destroyAllWindows()




def img_detection():
   img= cv2.imread(r"C:\Users\v.hariharasudhan\Desktop\ML Task\ml_project\assets\bottle_person.jpg")
   resizeimage=cv2.resize(img,(640,640),)
   results=model(resizeimage)[0]

   count=0

   cv2.imshow("resize Image",resizeimage)
   cv2.waitKey(0)

   print("Model ",model(resizeimage))
   print("Model Index",results)
   print("Model Box",results.boxes)


   for box in results.boxes:
        cls_id = int(box.cls[0])
        cls_name = model.names[cls_id]

        if cls_name == "bottle":  
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            cv2.rectangle(resizeimage, (x1, y1), (x2, y2), (0,255,0), 2)
            cv2.putText(resizeimage, f"Person,{count}", (x1, y1-10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,0), 2)
            count+=1
            cv2.imshow("Person Detection", resizeimage)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

   print(count)
   



"""
>>> img_detection() It is used from local image
>>> video_detection() It is used from live image 
"""



# 
# img_detection()







