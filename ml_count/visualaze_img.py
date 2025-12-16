import cv2 as cv

import pandas as pd
from matplotlib import pyplot as plt
from ultralytics import YOLO



# read_img=cv.imread(r"C:\Users\v.hariharasudhan\Desktop\ML Task\ml_count\dataset\images\train\gear\undamaged_gear\gear3.jpg")
# gray=cv.cvtColor(read_img,cv.COLOR_BGR2GRAY)
# cv.imshow("gray image",gray)



# plt.imshow(gray,cv.cvtColor(gray,cv.COLOR_GRAY2BGR))


# cv.waitKey(0)
# cv.destroyAllWindows()



# model=YOLO(r"C:\Users\v.hariharasudhan\Desktop\ML Task\ml_count\runs\detect\train\weights\best.pt")

# results=model.predict(source=r"C:\Users\v.hariharasudhan\Desktop\ML Task\ml_count\dataset\images\train\gear\rust_gears\bicycle-633208_1280.jpg")



data=pd.read_csv("C:\\Users\\v.hariharasudhan\\Desktop\\ML Task\\ml_count\\runs\detect\\train\\results.csv")
print(data['time'])

# results=model.train(data="dataset.yaml",epochs=100,imgsz=640)


model=YOLO("yolo11n.pt")






