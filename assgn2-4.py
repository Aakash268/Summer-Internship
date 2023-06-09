import cv2

# Read Image
img1 = cv2.imread('Assignment 2\Original Images\dog.jpg')
img2 = cv2.imread('Assignment 2\Original Images\\tree.jpg')
img3 = cv2.imread('Assignment 2\Original Images\Group.jpg')
dim1 = img1.shape
dim2 = img2.shape
dim3 = img3.shape
img2 = cv2.resize(img2, (int(dim2[1]*dim1[0]/dim2[0]),int(dim1[0])), interpolation= cv2.INTER_LINEAR)
img3 = cv2.resize(img3, (int(dim3[1]*dim1[0]/dim3[0]),int(dim1[0])), interpolation= cv2.INTER_LINEAR)
# Join two & three different images 
joinedImg = cv2.vconcat([img1, img2])
joinedImg = cv2.vconcat([joinedImg, img3])
# Show
cv2.imshow("Joined", joinedImg)
cv2.waitKey(0)
cv2.imwrite('Assignment 2\Processed Images\Joined\joinimg2.jpg',joinedImg)