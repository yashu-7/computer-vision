import cv2

# If you have multiple cameras change the number to 1,2... and to change the camera
default_cam_num = 0
cam = cv2.VideoCapture(default_cam_num)

while 1:
    ret, frame = cam.read()
    if not ret:
        break
    cv2.imshow("Camera Window", frame)
    
    if cv2.waitKey(1) & 0xff==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()