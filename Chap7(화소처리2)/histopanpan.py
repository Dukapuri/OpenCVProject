import numpy as np, cv2
from Common.histogram import draw_histo

image =  cv2.imread("../images/hist_stretch.jpg", cv2.IMREAD_GRAYSCALE)

hist = cv2.calcHist([image], [0], None, [256], [0, 256])

p_array = hist / sum(hist)
p_sum = 0
print(sum(hist),sum(p_array))
result_array = []
for s in p_array:
    p_sum += s
    result_array.append(p_sum * 255)

dst = [[result_array[val] for val in row] for row in image]
dst = np.array(dst, np.uint8)

original_hist = draw_histo(hist)
dst_hist = cv2.calcHist([dst], [0], None, [256], [0,256])
draw_hist = draw_histo(dst_hist)
cv2.imshow("original", image)
cv2.imshow("origin_hist", original_hist)
cv2.imshow("result", dst)
cv2.imshow("dst+hist", draw_hist)
cv2.waitKey(0)
