import cv2
import numpy as np
import os

kernel = np.ones((5,5), np.uint8)
directory = 'Assignment 2\Original Images'

for image in os.listdir(directory):
    # Read Image
    img = cv2.imread('Assignment 2\Original Images\\'+str(image))
    # Convert image into Gray, Blur, Canny, Dialation & Eroded image
    imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    # Gaussian Blur
    imgBlur = cv2.GaussianBlur(imgGray, (7,7), 0)

    # Canny
    imgCanny = cv2.Canny(imgBlur, 80, 200)

    # Dialation
    imgDial = cv2.dilate(imgCanny, kernel, iterations=1)

    # Erode
    imgErode = cv2.erode(imgDial, kernel, iterations=1)

    # Show
    cv2.imshow("Manipulated", imgErode)
    cv2.waitKey(0)
    cv2.imwrite('Assignment 2\Processed Images\Manipulated\edited'+ str(image),imgErode)
     