import cv2
import numpy as np


MODE = True  

def paint(event, x, y, flags, param):
    global MODE
    # print(MODE)

    if event == cv2.EVENT_LBUTTONDOWN:
        if MODE:
            cv2.circle(window, (x, y), 10, (0, 255, 0), -1)
        else:
            cv2.rectangle(window, (x - 10, y - 10), (x + 10, y + 10), (0, 255, 0), -1)


window = np.zeros((512, 512, 3), dtype=np.uint8)
cv2.namedWindow('window')
cv2.setMouseCallback('window', paint)

run = True
while run:
    cv2.imshow('window', window)
    k = cv2.waitKey(1) & 0xff
    if k == ord('q'):
        run = False
    elif k == ord('m'):
        MODE = not MODE  

cv2.destroyAllWindows()