import cv2


capture = cv2.VideoCapture(0)
if capture.isOpened() == False:
    raise Exception("카메라 연결 안됨")

def drawing_edge(th):
    rep_edge = cv2.GaussianBlur(rep_gray, (5, 5), 0)
    rep_edge = cv2.Canny(rep_edge, th, th*2, 5)
    h,w = frame.shape[:2]
    cv2.rectangle(rep_edge, (0,0,w,h), 255, -1)
    color_edge = cv2.bitwise_and(rep_image, rep_image, mask=rep_edge)
    cv2.imshow("color edge", color_edge)

th = 50
while True:
    ret, frame = capture.read()

    if not ret: break
    if cv2.waitKey(30) >= 0: break

    rep_image = cv2.repeat(frame, 1, 2)
    rep_gray = cv2.cvtColor(rep_image, cv2.COLOR_BGR2GRAY)
    drawing_edge(th)
    cv2.namedWindow("color edge", cv2.WINDOW_AUTOSIZE)

capture.release()