import cv2 as cv
img=cv.imread('image.png')
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gary',gray)

# BGR to hsv(hue-saturation-value):

hsv=cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.imshow('hsv',hsv)

# BGR to LAB(hue-saturation-value):
lab=cv.cvtColor(img,cv.COLOR_BGR2LAB)
cv.imshow('lab',lab)

# BGR to RGB:
rgb=cv.cvtColor(img,cv.COLOR_BGR2RGB)
cv.imshow('RGB',rgb)


cv.waitKey(0)