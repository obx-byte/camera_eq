import cv2 as cv 
import pandas as pd 
import numpy as nd
from matplotlib import pyplot as plt

from ultralytics import YOLO

import easyocr




# model=YOLO("yolov8n.pt")

# #train dataset
# model.train(data="dataset.yaml",epochs=100,imgsz=640 )



# # read image 

# read=cv.imread("C:\Users\v.hariharasudhan\Desktop\ML Task\ml_count\dataset\images\train\gear\undamaged_gear\Screenshot 2024-07-26 163943.jpg")
# cv.imshow("gray image ")
# cv.imshow()

# read_img=cv.imread(r"C:\Users\v.hariharasudhan\Downloads\1000134578.jpg")
# cv.imshow("original Image",cv.resize(read_img,(640,640)))
# resize=cv.resize(read_img,(640,640))
# gray=cv.cvtColor(resize,cv.COLOR_BGR2GRAY)
# blur1=cv.GaussianBlur(resize,(121,121),0)
# cv.imshow("gray",gray)
# cv.imshow("Gassian ",blur1)


# kernel=nd.array([[0,-1,0],[-1,5,-1],[0,-1,0]])
# sharp=cv.filter2D(resize,-1,kernel)



"""  EasyOCR"""
# import cv2
# import easyocr

# reader = easyocr.Reader(["en"], gpu=False)

# img = cv2.imread(r"C:\Users\v.hariharasudhan\Downloads\1000134578.jpg", cv2.IMREAD_GRAYSCALE)

# # Resize for clarity
# img = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)

# # Apply thresholding
# # _, img = cv2.threshold(img, 150, 255, cv2.THRESH_BINARY)


# print(img)
# results = reader.readtext(img)

# for _, text, confidence in results:
#     print(f"Text: {text}, Confidence: {confidence:.2f}")






import pytesseract
import cv2

img = cv2.imread(r"C:\Users\v.hariharasudhan\Downloads\1000134578.jpg", cv2.IMREAD_GRAYSCALE)
_, img = cv2.threshold(img, 150, 255, cv2.THRESH_BINARY)

custom_config = r'--oem 3 --psm 6 outputbase digits'
text = pytesseract.image_to_string(img, config=custom_config)
print("Digits:", text)




cv.waitKey(0)
cv.destroyAllWindows()



















