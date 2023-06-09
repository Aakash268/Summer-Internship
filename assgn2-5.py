import cv2

faceCascade = cv2.CascadeClassifier("Assignment 2\haarcascades\haarcascade_frontalface_alt.xml")

img = cv2.imread("Assignment 2\Original Images\Group.jpg")
imgGrey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = faceCascade.detectMultiScale(imgGrey, 1.1, 8)

for (x,y,w,h) in faces:
    cv2.rectangle (img, (x,y), (x+w, y+h), (0,255,0), 1)

cv2.imshow("Result", img)
cv2.imwrite('Assignment 2\Processed Images\Face Detected\detectedface.jpg',img)
cv2.waitKey(0)