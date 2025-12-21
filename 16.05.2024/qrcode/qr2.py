from __future__ import print_function
import pyzbar.pyzbar as pyzbar
import numpy as np
import cv2
import time
import psycopg2
import parameter
import re
# get the webcam:  
cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
#160.0 x 120.0
#176.0 x 144.0
#320.0 x 240.0
#352.0 x 288.0 #hh
#640.0 x 480.0
#1024.0 x 768.0
#1280.0 x 1024.0
#time.sleep(1)
def decode(im) : 
    decodedObjects = pyzbar.decode(im)  
    for obj in decodedObjects:        
        obj_type = obj.type
        print('Type1 : ', obj_type)
        objdata = str(obj.data)

        res_data = re.findall(r"[A-Za-z0-9]{20}",objdata)
        data = str(res_data)
        data1 = data.split()
        resset = data1[0].strip('['',')
        resset1 = resset.strip("']")                                                                                                                                                        
        print('Data1 : ', resset1,'\n' )  
        conn = psycopg2.connect(database = 'qrcode' , user = 'postgres' ,password = 'postgres' , host ='10.17.19.85' ,port ='5432')
        cursor = conn.cursor()
        cursor.execute("select data , ondate from public.qrcodetable where data ='%s' and to_char(ondate,'yyyy-mm-dd H:M:S') = to_char(now(),'yyyy-mm-dd H:M:S')")
        if cursor.rowcount == 0:
          print("Data Already Exists")           
        else:
            sql = "INSERT INTO public.qrcodetable(type, data) VALUES('"+str(obj_type)+"','"+str(resset1)+"')"
            cursor.execute(sql)
            print(sql)
            conn.commit()
    return decodedObjects
font = cv2.FONT_HERSHEY_SIMPLEX
while(cap.isOpened()):
    ret, frame = cap.read()
    im = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    decodedObjects = decode(im)
    for decodedObject in decodedObjects: 
        points = decodedObject.polygon
        if len(points) > 4 : 
          hull = cv2.convexHull(np.array([point for point in points], dtype=np.float32))
          hull = list(map(tuple, np.squeeze(hull)))
        else : 
          hull = points
        n = len(hull)     
        for j in range(0,n):
          cv2.line(frame, hull[j], hull[ (j+1) % n], (255,0,0), 3)
        x = decodedObject.rect.left
        y = decodedObject.rect.top
        print(x, y)
        print('Type2 : ', decodedObject.type)
        print('Data2 : ', decodedObject.data,'\n')
        Code2 = str(decodedObject.data)
        res_data1 = re.findall(r"[A-Za-z0-9]{40}",Code2)
        data1 = str(res_data1)
        data1 = data1.split()
        resset_2 = data1[0].strip('['',')
        resset2 = resset_2.strip("']")                                                                                                                                                        
        print('Data2 : ', resset2,'\n' )  
        conn = psycopg2.connect(database = 'qrcode' , user = 'postgres' ,password = 'postgres' , host ='10.17.19.85' ,port ='5432')
        cursor = conn.cursor()
        cursor.execute("select data , ondate from public.qrcodetable where data ='%s' and to_char(ondate,'yyyy-mm-dd H:M:S') = to_char(now(),'yyyy-mm-dd H:M:S')")
        if cursor.rowcount == 0:
          print("Data Already Exists")           
        else:
          sql = "INSERT INTO public.qrcodetable(type, data) VALUES('"+str(Code2)+"','"+str(resset2)+"')"
          cursor.execute(sql)
          print(sql)
          conn.commit()
        cv2.putText(frame, Code2, (x, y), font, 1, (0,255,255), 2, cv2.LINE_AA)
    cv2.imshow('frame',frame)
    key = cv2.waitKey(1)
    if key & 0xFF == ord('q'):
        break
    elif key & 0xFF == ord('s'): 
        cv2.imwrite('Capture.png', frame)     
cap.release()
cv2.destroyAllWindows()

 