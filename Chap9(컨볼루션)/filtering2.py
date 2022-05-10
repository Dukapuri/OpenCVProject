import numpy as np, cv2

def quadratic_differential(image):
    rows, cols = image.shape[:2]
    mask_y = [[-1, 0, 1],
              [-2, 0, 2],
              [-1, 0, 1]]
    mask_x = [[-1, -2, -1],
              [0, 0, 0],
              [1, 2, 1]]
    mask_x = np.array(mask_x, np.float32)
    mask_y = np.array(mask_y, np.float32)
    ans_imagex = np.zeros((rows, cols), np.float32)
    ans_imagey = np.zeros((rows, cols), np.float32)
    ycenter, xcenter = mask_x.shape[0] //2, mask_x.shape[1]//2

    for i in range(ycenter, rows - ycenter):
        for j in range(xcenter, cols - xcenter):
            sumx = 0.0
            sumy = 0.0
            for u in range(mask_x.shape[0]):
                for v in range(mask_x.shape[1]):
                    y, x = i + u - ycenter, j + v - xcenter
                    sumx += image[y, x] * mask_x[u, v]
                    sumy += image[y, x] * mask_y[u, v]
            ans_imagex[i, j] = sumx
            ans_imagey[i, j] = sumy

    return cv2.sqrt(cv2.pow(ans_imagex, 2) + cv2.pow(ans_imagey, 2))

image = cv2.imread("../images/laplacian.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상파일 읽기 오류")

filter_image = quadratic_differential(image)
filter_image = cv2.convertScaleAbs(filter_image)

cv2.imshow("image", image)
cv2.imshow("filter_image", filter_image)
cv2.waitKey(0)
