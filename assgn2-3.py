import cv2
import os
from random import randrange

directory = 'Assignment 2\Original Images'
res = (1920,1080)
for image in os.listdir(directory):
    # Read Image
    img = cv2.imread('Assignment 2\Original Images\\'+str(image))
    dim = img.shape
    # Insertion of shapes (rectangle & circle) in the given image  
    
    # Rectangle
    cv2.rectangle(img, (randrange(dim[1]), randrange(dim[0])), (randrange(dim[1]), randrange(dim[0])), (0,0,255), 2)

    # Circle
    cv2.circle(img, (randrange(dim[1]), randrange(dim[0])), randrange(20), (255,255,0), 3)
    # Show
    cv2.imshow("Drawn", img)
    cv2.waitKey(0)
    cv2.imwrite('Assignment 2\Processed Images\Drawn'+ str(image),img)