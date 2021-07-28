import numpy as np
import cv2 as cv
from  matplotlib import pyplot as plt

img1 = cv.imread('D:\Machine Vision\image\japanese temple.jpg', 1)
img2 = cv.imread('D:\Machine Vision\image\japanese temple.jpg', 0)
img3 = cv.imread('D:\Machine Vision\image\japanese temple.jpg', -1)
img4 = cv.imread('D:\Machine Vision\image\japanese temple.jpg', cv.IMREAD_COLOR)
img5 = cv.imread('D:\Machine Vision\image\japanese temple.jpg', cv.IMREAD_GRAYSCALE)
img6 = cv.imread('D:\Machine Vision\image\japanese temple.jpg', cv.IMREAD_UNCHANGED)

cv.namedWindow('image', cv.WINDOW_NORMAL)
cv.imshow('image', img1)
k = cv.waitKey(0) & 0xff
if k == 27:
    cv.destroyAllWindows()
if k == ord('s'):
    cv.imwrite('gray jtemple.png', img5)
    cv.destroyAllWindows()

plt.subplot(321), plt.imshow(img1), plt.title('1')
plt.subplot(322), plt.imshow(img2), plt.title('0')
plt.subplot(323), plt.imshow(img3), plt.title('-1')
plt.subplot(324), plt.imshow(img4), plt.title('color')
plt.subplot(325), plt.imshow(img5), plt.title('gray')
plt.subplot(326), plt.imshow(img6), plt.title('unchanged')

plt.show()
