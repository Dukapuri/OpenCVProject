import numpy as np, cv2

def scaling(img, size):
    dst = np.zeros(size[::-1], img.dtype)
    ratioY, ratioX = np.divide(size[::-1], img.shape[:2])
    for i in range(0, size[1]):
        for j in range(0, size[0]):
            y, x = np.int32(i / ratioY), np.int32(j / ratioX)
            dst[i, j] = img[y, x]
    return dst

# def scaling2(img, size):
#     dst = np.zeros(size[::-1], img.dtype)
#     ratioY, ratioX = np.divide(size[::-1], img.shape[:2])
#     i = np.arange(0, size[1], 1)
#     j = np.arange(0, size[0], 1)
#     i, j = np.meshgrid(i, j)
#     y, x = np.int32(i / ratioY), np.int32(j / ratioX)
#     dst[i, j] = img[y, x]
#     return dst

image = cv2.imread("../images/scaling.jpg", cv2.IMREAD_GRAYSCALE)
dst1 = scaling(image, (350, 400))
dst2 = scaling(image, (600, 900))
# dst3 = scaling2(image,(600, 900))
cv2.imshow("image", image)
cv2.imshow("dst", dst1)
cv2.imshow("dst2", dst2)
# cv2.imshow("dst3", dst3)
cv2.waitKey(0)

