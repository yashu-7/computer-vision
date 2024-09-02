import cv2
import math
import numpy as np

def draw_circle(event, x, y, flags, param):
    global drawing, px, py, radius, circles

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True  
        px, py = x, y  

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            radius = math.sqrt((x - px) ** 2 + (y - py) ** 2)
            redraw_circles()
            cv2.circle(window, (px, py), int(radius), (0, 255, 0), 3)
            cv2.imshow('window', window) 

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False  
        radius = math.sqrt((x - px) ** 2 + (y - py) ** 2)
        circles.append((px, py, int(radius)))  
        redraw_circles()

def redraw_circles():
    window.fill(0) 
    for circle in circles:
        cv2.circle(window, (circle[0], circle[1]), circle[2], (0, 255, 0), -1)
    cv2.imshow('window', window)

drawing = False
px, py = None, None
circles = []  

window = np.zeros((512, 512, 3), dtype=np.uint8)
cv2.namedWindow('window')
cv2.setMouseCallback('window', draw_circle)

run = True
while run:
    cv2.imshow('window', window)
    k = cv2.waitKey(1) & 0xff
    if k == ord('q'):
        run = False

cv2.destroyAllWindows()