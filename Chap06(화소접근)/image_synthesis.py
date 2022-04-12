import numpy as np,cv2

image1 = cv2.imread("../images/add1.jpg", cv2.IMREAD_GRAYSCALE)
image2 = cv2.imread("../images/add2.jpg", cv2.IMREAD_GRAYSCALE)

if image1 is None or image2 is None: raise Exception("영상파일 읽기 오류")

##영상 합성 방법
alpha, beta = 0.6, 0.7
add_image1 = cv2.add(image1, image2)
add_image2 = cv2.add(image1 * alpha, image2 * beta)
add_image2 = np.clip(add_image2, 0,255).astype('uint8')
add_image3 = cv2.addWeighted(image1, alpha, image2, beta, 0)

titles = ['image1', 'image2', 'add_image1', 'add_image2', 'add_image3']
for t in titles: cv2.imshow(t, eval(t))
cv2.waitKey(0)