import glob
import cv2
import pandas as pd
import pathlib
def read_qr_code(filename):
        img = cv2.imread(filename)
        detect = cv2.QRCodeDetector()
        value, points, straight_qrcode = detect.detectAndDecode(img)
        return value
value = read_qr_code(r'C:\Users\s.devi\Desktop\qrcode\MyQRCode1.png')
print(value)
