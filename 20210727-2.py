import cv2
import numpy as np
from matplotlib import pyplot as plt
def bgr2rbg(img):
    '''
        将颜色空间从BGR转换为RBG
    '''
    return img[:,:,::-1]

#開圖
img = cv2.imread('D:\Machine Vision\image\japanese temple.jpg')
cv2.namedWindow('img1')
img1 = cv2.resize(img,None,fx=10,fy=10,interpolation=cv2.INTER_CUBIC)
img5 = cv2.resize(img,None,fx=1/100,fy=1/100,interpolation=cv2.INTER_CUBIC)
img2 = img[:,::-1] 
img3 = img[::-1]
img4 = img[::-1, ::-1]
img6 = img5[:,::-1] 
img7 = img5[::-1]
img8 = img5[::-1, ::-1]

#秀圖
plt.subplot(421)
plt.title('SRC')
plt.imshow(bgr2rbg(img1))

plt.subplot(422)
plt.title('Horizontally')
plt.imshow(bgr2rbg(img2))

plt.subplot(423)
plt.title('Vertically')
plt.imshow(bgr2rbg(img3))

plt.subplot(424)
plt.title('Horizontally & Vertically')
plt.imshow(bgr2rbg(img4))

plt.subplot(425)
plt.title('SRC')
plt.imshow(bgr2rbg(img5))

plt.subplot(426)
plt.title('Horizontally')
plt.imshow(bgr2rbg(img6))

plt.subplot(427)
plt.title('Vertically')
plt.imshow(bgr2rbg(img7))

plt.subplot(428)
plt.title('Horizontally & Vertically')
plt.imshow(bgr2rbg(img8))

plt.show()