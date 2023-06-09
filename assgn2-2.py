import cv2
import os

directory = 'Assignment 2\Original Images'
res = (1920,1080)
for image in os.listdir(directory):
    # Read Image
    img = cv2.imread('Assignment 2\Original Images\\'+str(image))
    dim = img.shape
    # Resize image into: (i) Smaller than original & (ii) Upto to screen size 

    # (i) Smaller than original
    imgresizes = cv2.resize(img, (int(3*dim[1]/4),int(3*dim[0]/4)), interpolation= cv2.INTER_LINEAR)
    # (ii) Upto screen size
    imgresizel = cv2.resize(img, (res[0],res[1]), interpolation= cv2.INTER_LINEAR)
    # Show
    cv2.imshow("ResizedSmall", imgresizes)
    cv2.waitKey(0)
    cv2.imshow("ResizedBig", imgresizel)
    cv2.waitKey(0)
    cv2.imwrite('Assignment 2\Processed Images\Resized\editedsmall'+ str(image),imgresizes)
    cv2.imwrite('Assignment 2\Processed Images\Resized\editedbig'+ str(image),imgresizel)