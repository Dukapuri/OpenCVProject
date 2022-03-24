import cv2
def put_string(fram, text, pt, value, color=(120,200,90)):
    text += str(value)
    shade = (pt[0] + 2, pt[1] + 2)
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(fram, text, shade, font, 0.7, (0,0,0), 2)
    cv2.putText(fram, text, pt   , font, 0.7, color, 2)
