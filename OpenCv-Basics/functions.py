import cv2 as cv
img=cv.imread('image.png')
cv.imshow('image',img)

# converting img to grayscale:
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)

# bluring an image:
blur=cv.GaussianBlur(img,(3,3),cv.BORDER_DEFAULT)
cv.imshow('blur',blur)

# Edges Cascade:

canny=cv.Canny(blur,125,175)
cv.imshow("canny",canny)   

# passing the real iamges produces a lot of noise that can be detected as an edge which can affect the result. so we instead pass the blur of that og imgae.

# dilation :
dial=cv.dilate(canny,(8,8),iterations=3)
cv.imshow('dilate',dial)


#Dilation helps fill small holes or gaps in objects, especially if a shape is broken or has tiny imperfections.

# Example:

# If you have broken text or outlines, dilation can reconnect the gaps.


#errosion:
errode=cv.erode(dial,(3,3),iterations=3)
cv.imshow('errode',errode)


# resize:
resized = cv.resize(img,(500,500),interpolation=cv.INTER_AREA)
cv.imshow('resize',resized)

# cropping: consider an image as an array of pixels, so we can select an range of pixles from that array to get the cropped version.

cropped=img[50:500,200:400]
cv.imshow('cropped',cropped)


cv.waitKey(0)
