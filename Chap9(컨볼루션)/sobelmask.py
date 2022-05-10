import numpy as np, cv2

def sobelMask2D(img, mask):



image = cv2.imread("../images/laplacian.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상파일 읽기 오류")


filter_image = sobelMask2D(image)
xmask =
filter_image = cv2.convertScaleAbs(filter_image)

cv2.imshow("image", image)
cv2.imshow("filter_image", filter_image)
cv2.waitKey(0)
