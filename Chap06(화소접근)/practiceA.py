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

def search_value_idx(hist, bior = 0):
    for i in range(hist.shape[0]):
        idx = np.abs(bior - i)
        if hist[idx] > 0: return idx
    return -1

image = cv2.imread("../images/hist_stretch.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상 입력 오류")

bsize, ranges = 64, [0,256]
image_hist = calc_histo(image, bsize, ranges)
gap = ranges[1] / bsize

low = search_value_idx(image_hist, 0) * gap
high = search_value_idx(image_hist, image_hist.shape[0] - 1) * gap

idx = np.arange(0,256)
idx = (idx - low)/(high - low) * 255
idx[:int(low)] = 0
idx[int(high):] = 255

dst = np.zeros(image.shape,image.dtype)
for i in range(dst.shape[0]):
    for j in range(dst.shape[1]):
        dst[i,j] = idx[image[i,j]]


hist_image = draw_histo(image_hist)
dst_hist = calc_histo(dst, bsize, ranges)
dst_hist_image = draw_histo(dst_hist)

cv2.imshow("image", image)
cv2.imshow("image_hist", hist_image)
cv2.imshow("dst", dst)
cv2.imshow("dst_hist", dst_hist_image)
cv2.waitKey(0)