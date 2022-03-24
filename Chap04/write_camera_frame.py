import cv2

capture = cv2.VideoCapture(0)
if capture.isOpened() == False:raise Exception("카메라 연결 안됨")

fps = 29.97