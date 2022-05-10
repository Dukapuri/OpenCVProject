import numpy as np, cv2
from Common.filters import filter

image = cv2.imread("../images/laplacian.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상파일 읽기 오류")

blur_mask = [1 / 9 for _ in range(9)]
sharpe_mask = [[0, -1, 0],
               [-1, 5, -1],
               [0, -1, 0]]
line_mask = [[-1, 0, 1],
             [-1, 0, 1],
             [-1, 0, 1]]

#마스크 만들기
blur_mask = np.array(blur_mask, np.float32).reshape(3, 3)
sharpe_mask = np.array(sharpe_mask, np.float32)
line = np.array(line_mask, np.int16)


blur = filter(image, blur_mask)
sharp = filter(image, sharpe_mask)
line = cv2.filter2D(image, cv2.CV_16S, line)

cv2.imshow("image", image)
cv2.imshow("blur", blur.astype('uint8'))
cv2.imshow("sharp", cv2.convertScaleAbs(sharp))
cv2.imshow("line", cv2.convertScaleAbs(line))
cv2.waitKey(0)
