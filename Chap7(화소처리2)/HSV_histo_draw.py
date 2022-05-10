import numpy as np, cv2

def cal2_histo(HSV_image):
    hue, saturation, bright = cv2.split(HSV_image)
    hue_hist = cv2.calcHist([hue], [0], None, [180], [0, 180])
    saturation_hist = cv2.calcHist([saturation], [0], None, [256], [0, 256])
    new_hist = np.zeros((hue_hist.shape[0], saturation_hist.shape[0]), np.uint8)

    for row in HSV_image:
        for pix in row:
            new_hist[pix[0]][pix[1]] += 1
    return new_hist

def draw_hist(hist):
    hist_img = np.full(hist.shape[:2], 255, np.uint8)
    gapx = 1
    gapy = 1

    for i in range(hist.shape[1]):
        for j in range(hist.shape[0]):
            x = (i, j)  #시작좌표
            y = (i + 1, j + 1)
            cv2.rectangle(hist_img, x,y, cv2.cvtColor(np.array([i,j,hist[i][j]], np.uint8), cv2.COLOR_HSV2BGR), cv2.FILLED)

BGR_image = cv2.imread("../images/contrast.jpg", cv2.IMREAD_COLOR)
if BGR_image is None: raise Exception("영상파일 읽기 오류")

HSV_image = cv2.cvtColor(BGR_image, cv2.COLOR_BGR2HSV)
histo = cal2_histo(HSV_image)

draw_histo = draw_hist(histo)

# cv2.imshow("image", BGR_image)
# cv2.imshow("hist", draw_histo)
# cv2.waitKey(0)