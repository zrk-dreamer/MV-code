import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('D:\Machine Vision\image\japanese temple.jpg')

L1 = cv.pyrDown(img)
L2 = cv.pyrDown(L1)
L3 = cv.pyrDown(L2)
L4 = cv.pyrDown(L3)

U1 = cv.pyrUp(L4)
U2 = cv.pyrUp(L3)
U3 = cv.pyrUp(L2)
U4 = cv.pyrUp(L1)

print(img.shape, U4.shape)

sub = img - U4

plt.subplot(521), plt.imshow(img)
plt.subplot(522), plt.imshow(L1)
plt.subplot(523), plt.imshow(L2)
plt.subplot(524), plt.imshow(L3)
plt.subplot(525), plt.imshow(L4)
plt.subplot(526), plt.imshow(L4)
plt.subplot(527), plt.imshow(U1)
plt.subplot(528), plt.imshow(U2)
plt.subplot(529), plt.imshow(U3)
plt.show()
plt.subplot(211), plt.imshow(img)
plt.subplot(212), plt.imshow(sub)
plt.show()
