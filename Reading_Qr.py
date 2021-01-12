from cv2 import cv2
import numpy as np
from pyzbar.pyzbar import decode

#img  =  cv2.imread("v.png")
cap  = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
cap.set(10,150)
#code = decode(img)

while True:

    success,img = cap.read()


    for barcode in decode(img):
        print(barcode.data)
        myData = barcode.data.decode('utf-8')
        print(myData)

        points = np.array([barcode.polygon],np.int32)
        points = points.reshape(-1,1,2)
        cv2.polylines(img,[points],True,(255,0,0),10)
        points2 = barcode.rect
        cv2.putText(img,myData,(points2[0],points2[1]),cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,0,0),2)


    cv2.imshow("Result",img)
    cv2.waitKey(1)
#cv2.imshow("vaibhav",img)
#print(code)
#cv2.waitKey(0)