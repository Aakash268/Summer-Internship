import cv2

# Read and Save Video
cap = cv2.VideoCapture("sample-1.mp4")

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640,480))

frameWidth = 640
frameHeight = 480
while True:
    success, img = cap.read()
    img = cv2.resize(img, (frameWidth,frameHeight))
    out.write(img)

    cv2.imshow("Video", img)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()