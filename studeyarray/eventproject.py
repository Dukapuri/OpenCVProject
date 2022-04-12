import numpy as np,cv2

from studeyarray.arithmethic_op import m_mask

image = cv2.imread("images/flip_text.jpg", cv2.IMREAD_COLOR)
if image is None: raise Exception("영상 파일 읽기 오류")

# mask[60:160, 20:120] = 50
m_mask = np.zeros(image.shape[:2], np.uint8)

m_mask[600:700,300:400] = 255


avg = cv2.mean(image,m_mask)



# print(mean_value1)
#
# for kk in range(60,161):
#     for jj in range(20,120):
#         image[kk][jj] += 50;
#
# for kk in range(300,400):
#     for jj in range(200,300):
#         for pp in range(len(image[kk][jj])):
#             if image[kk][jj][pp] >= 127:
#                 image[kk][jj][pp] += 20
#             if image[kk][jj][pp] < 127:
#                 image[kk][jj][pp] -= 20

for kk in range(300,800):
    for jj in range(300,600):
        for pp in range(len(image[kk][jj])):
            if image[kk][jj][pp] >= avg[pp]:
                image[kk][jj][pp] = image[kk][jj][pp] - avg[pp]
            if image[kk][jj][pp] < avg[pp]:
                image[kk][jj][pp] = image[kk][jj][pp] - avg[pp]

cv2.imshow("image", image)
# for kk in range(600,700):
#     for jj in range(300,400):
#         for pp in range(len(image[kk][jj])):
#             if image[kk][jj][pp] >= 127:
#                 image[kk][jj][pp] += 20
#             if image[kk][jj][pp] < 127:
#                 image[kk][jj][pp] -= 20

# cv2.imshow("image", ans_image)

cv2.waitKey(0)