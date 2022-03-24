import numpy as np
import cv2
line = 1
circleRadius = 1
def onMouse(event, x, y, flags, param):
    global title, pt, line, circleRadius
    if event == cv2.EVENT_LBUTTONDOWN:
        if pt[0] < 0: pt = (x, y)
        point = (x + 30, y + 30)
        cv2.rectangle(image, pt, point, (255,0,0,) , line)
        cv2.imshow(title, image)
        pt = (-1, -1)
    elif event == cv2.EVENT_RBUTTONDOWN:
        if pt[0] < 0: pt = (x , y)
        radius = 20;
        cv2.circle(image, pt, circleRadius, (0,255,0), line)
        cv2.imshow(title, image)
        pt = (-1,-1)

def onLineWeight(value):
    global line

    add_value = value - line
    line += add_value

def onCircleRadius(value):
    global circleRadius

    add_value = value - circleRadius
    circleRadius += add_value



pt = (-1,-1)

image =  np.full((400,600,3),(255,255,255), np.uint8)
title = "Draw Event"
cv2.imshow(title, image)
cv2.setMouseCallback(title, onMouse)
cv2.createTrackbar('LineWeight', title,line, 10, onLineWeight)
cv2.createTrackbar('CircleRadius', title, circleRadius, 50, onCircleRadius)
cv2.waitKey(0)
# cv2.destroyAllWindows()