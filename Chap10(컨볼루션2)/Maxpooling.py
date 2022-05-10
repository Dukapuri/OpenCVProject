import numpy as np, cv2

def found_Max(arr):
    return np.max(arr)


def maxPooling(image):
    rows, cols = image.shape[:2]
    dst = np.zeros((rows//2,cols//2), np.uint8)

    for k in range(0, rows, 2):
        for p in range(0, cols , 2):
            dst[k//2,p//2]= max(image[k:k+1,p:p+1])

    return dst

image = cv2.imread("../images/laplacian.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상파일 읽기 오류")

filter_image = maxPooling(image)

cv2.imshow("image", image)
cv2.imshow("filter_image", filter_image)
cv2.waitKey(0)