import cv2
from pyzbar.pyzbar import decode
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    results = decode(frame)
    for result in results: 
        x, y, w, h = result.rect
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        print('Result : ',result.data.decode("utf-8"))
    cv2.imshow("QR Code Scanner", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()

