import cv2 as cv
img1 = cv.imread('D:\Machine Vision\image\OIP.jpg', 0)
cv.namedWindow('image', cv.WINDOW_NORMAL)
cv.imshow('image', img1)
cv.waitKey(0)
cv.destroyAllWindows