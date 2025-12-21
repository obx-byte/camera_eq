import cv2
import numpy as np
from PIL import Image
import pytesseract
import re

# Connect to the network camera stream
camera = cv2.VideoCapture(r"rtsp://admin:Vi$ualins0324@192.168.196.225:554/Streaming/Channels/1")

# Detecting numberplate
def number_plate_detection(img):
    # Your number plate detection code here...
    # This function should detect number plates in the given image and return the detected number plate.
    # You can use OpenCV, image processing techniques, or any other library or method for number plate detection.

    # Placeholder return for now
    return "ABC1234"  # Replace this with your actual number plate detection result

# Quick sort function
def quickSort(arr, low, high):
    # Your quick sort implementation...
    pass  # Placeholder for quick sort implementation

# Binary search function
def binarySearch(arr, low, high, x):
    # Your binary search implementation...
    pass  # Placeholder for binary search implementation

print("HELLO!!")
print("Welcome to the Number Plate Detection System.\n")

previous_plate = None  # Initialize previous_plate to None

while True:
    # Capture frame-by-frame
    ret, frame = camera.read()

    # Check if the frame is None
    if frame is None:
        break

    cv2.imshow("Camera Stream", frame)

    # Perform number plate detection on the frame
    number_plate = number_plate_detection(frame)
    if number_plate:
        res2 = str("".join(re.split("[^a-zA-Z0-9]*", number_plate)))
        res2 = res2.upper()
        print(res2)

        # Sorting
        if previous_plate is not None and res2 < previous_plate:
            temp = previous_plate
            previous_plate = res2
            res2 = temp

        print("\n\n")
        print("The Vehicle numbers registered are:-")
        print(previous_plate)
        print(res2)
        print("\n\n")

        # Searching
        # Assume you have a separate function for searching new plates and checking if they're allowed to visit
        # Here you can use the binary search function to check if the new plate is allowed
        result = binarySearch(previous_plate, res2, res2, res2)
        if result != -1:
            print("\n\nThe Vehicle is allowed to visit.")
        else:
            print("\n\nThe Vehicle is not allowed to visit.")

        previous_plate = res2  # Update previous_plate with the latest plate

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
camera.release()
cv2.destroyAllWindows()
