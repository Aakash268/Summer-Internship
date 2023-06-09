import cv2
from PIL import Image 
import pytesseract
  
def ocr_core(img):
    text = pytesseract.image_to_string(Image.open(img))
    return text

im = Image.open('Assignment 3\Original Images\\try1.jpg')

left = 562
top = 550
right = 900
bottom = 610
  
# im = im.rotate(6)
im = im.crop((left, top, right, bottom)) 
  
im.save("Assignment 3\Processed Images\\cropped1.jpg")
print(ocr_core("Assignment 3\Processed Images\\cropped1.jpg"))


img = cv2.imread('Assignment 3\Processed Images\\cropped1.jpg')
mser = cv2.MSER_create()

#Resize the image so that MSER can work better
img = cv2.resize(img, (img.shape[1]*2, img.shape[0]*2))
# img = img[5:-5,5:-5,:]

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
vis = img.copy()

regions = mser.detectRegions(gray)

hulls = [cv2.convexHull(p.reshape(-1, 1, 2)) for p in regions[0]]
cv2.polylines(vis, hulls, 1, (0,255,0)) 

cv2.imwrite("Assignment 3\Processed Images\\processed1.jpg",vis)
cv2.namedWindow('image', 0)

cv2.imshow('image', vis)
while(cv2.waitKey(0)!=ord('q')):
       continue
cv2.destroyAllWindows()