import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
def nothing(x):
    pass

img = cv.imread('D:\Machine Vision\image\test1.jpg', 0)
cv.namedWindow('image1')
cv.createTrackbar('min', 'image1', 0, 255, nothing)
cv.createTrackbar('max', 'image1', 0, 255, nothing)
cv.imshow('image1', img)

while True:
    min = cv.getTrackbarPos('min', 'image1')
    max = cv.getTrackbarPos('max', 'image1')
    edges = cv.Canny(img, min, max)
    cv.imshow('canny', edges)
    if cv.waitKey(1) == 27:
        break
cv.destroyAllWindows
    
