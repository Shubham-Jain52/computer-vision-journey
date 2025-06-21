import cv2 as cv
import numpy as np

img=cv.imread('image.png')
blank=np.zeros(img.shape,dtype='uint8')
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# cv.imshow('gray',gray)


blur=cv.GaussianBlur(gray,(5,5),cv.BORDER_DEFAULT)
cv.imshow('blur',blur)


# canny=cv.Canny(blur,125,175)
# cv.imshow('canny',canny)

#instead of using canny for the edges, we can use the threshold

#threshold:
ret, thresh=cv.threshold(gray,125,225,cv.THRESH_BINARY)
cv.imshow('threshold',thresh)

# 0----> black
# 1----> white



# finding contours:
contours, hierarchies=cv.findContours(thresh,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
cv.drawContours(blank,contours,-1,(0,0,255),2)
cv.imshow('contourOnBlank',blank)
print(f"number of contours :{len(contours)}")

cv.waitKey(0)