import numpy as np, cv2
from Common.histogram import draw_histo


def calc_histo(image, histSize, range=[0,256]):
    hist = np.zeros((histSize, 1), np.float32)
    gap = range[1]/histSize

    for row in image:
        for pix in row:
            idx = int(pix/gap)
            hist[idx] += 1

    return hist

def search_value_idx(hist, biar = 0):
    for i in range(hist.shape[0]):
        idx = np.abs(biar - i)
        if hist[idx] > 0: return idx
    return -1

image = cv2.imread("../images/hist_stretch.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상 입력 오류")

first_section = [12,76]

second_section = [150,250]

bsize, ranges = 256, [0,256]
image_hist = calc_histo(image, bsize, ranges)
gap = ranges[1] / bsize


low = search_value_idx(image_hist, 0) * gap
high = search_value_idx(image_hist, bsize - 1) * gap


original_section = [low,high]


idx = np.arange(0,256)
idx = ((idx - original_section[0]) * ((first_section[1] - first_section[0]) / (original_section[1] - original_section[0]))) + first_section[0]
idx[:int(low)] = 0
idx[int(high + 1):] = 255

idx2 = np.arange(0,256)
idx2 = ((idx2 - original_section[0]) * ((second_section[1] - second_section[0]) / (original_section[1] - original_section[0]))) + second_section[0]
idx2[:int(low)] = 0
idx2[int(high + 1):] = 255

dst = np.zeros(image.shape, image.dtype)
for i in range(dst.shape[0]):
    for j in range(dst.shape[1]):
        dst[i,j] = idx[image[i,j]]

#dst2 이미지 만들어주기#
dst2 = np.zeros(image.shape, image.dtype)
for i in range(dst2.shape[0]):
    for j in range(dst2.shape[1]):
        dst2[i,j] = idx2[image[i,j]]


hist_image = draw_histo(image_hist)
dst_hist = calc_histo(dst, bsize, ranges)
dst_hist_image = draw_histo(dst_hist)
dst2_hist = calc_histo(dst2, bsize, ranges)
dst2_hist_image = draw_histo(dst2_hist)


cv2.imshow("image", image)
cv2.imshow("image_hist", hist_image)
cv2.imshow("dst", dst)
cv2.imshow("dst_hist", dst_hist_image)
cv2.imshow("dst2", dst2)
cv2.imshow("dst2_hist", dst2_hist_image)
cv2.waitKey(0)