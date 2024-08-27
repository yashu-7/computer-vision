import cv2
import numpy as np
import math

img_path = r'Projects\IMG_20240827_113204694.jpg'

img = cv2.imread(img_path)

DIAGONAL_CM = 36.83 
SCREEN_RESOLUTION = (1920, 1080)  

aspect_ratio = SCREEN_RESOLUTION[0] / SCREEN_RESOLUTION[1]
height_cm = math.sqrt((DIAGONAL_CM ** 2) / (1 + aspect_ratio ** 2))
width_cm = height_cm * aspect_ratio

PIXEL_SIZE = width_cm / SCREEN_RESOLUTION[0]
DISTANCE = 10  

def colour_classifier(img):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower_green = np.array([30, 50, 50])
    upper_green = np.array([90, 255, 255])
    mask = cv2.inRange(hsv, lower_green, upper_green)
    out_img = cv2.bitwise_and(img, img, mask=mask)
    return out_img, mask

def scale_img(img, scale_factor=0.15):
    WIDTH, HEIGHT = img.shape[1], img.shape[0]
    new_w = int(WIDTH * scale_factor)
    new_h = int(HEIGHT * scale_factor)
    img = cv2.resize(img, (new_w, new_h))
    return img

def draw_bounding_boxes(img, mask):
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 30:
            rect = cv2.minAreaRect(cnt)
            box = cv2.boxPoints(rect)
            box = np.intp(box)
            cv2.drawContours(img, [box], 0, (0, 255, 0), 2)
            
            width = np.linalg.norm(box[0] - box[1]) * PIXEL_SIZE * DISTANCE / 10
            height = np.linalg.norm(box[0] - box[3]) * PIXEL_SIZE * DISTANCE / 10
            
            cv2.putText(img, f"Height: {width:.2f} cm", (int(box[0][0]), int(box[0][1])), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (150, 180, 255), 2)
            cv2.putText(img, f"Width: {height:.2f} cm", (int(box[0][0]), int(box[0][1]) + 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (150, 180, 255), 2)
            
    return img

img = scale_img(img, scale_factor=0.15)
masked_img, mask = colour_classifier(img)
img_with_boxes = draw_bounding_boxes(img.copy(), mask)

cv2.imshow('Original Image', img)
cv2.imshow('Masked Image', masked_img)
cv2.imshow('Image with Bounding Boxes', img_with_boxes)
cv2.waitKey(0)
cv2.destroyAllWindows()