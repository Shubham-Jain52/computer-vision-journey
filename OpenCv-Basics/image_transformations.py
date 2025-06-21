import cv2 as cv
import numpy as np

img=cv.imread('image.png')
cv.imshow('og',img)
def trans(img,x,y):
    transMat=np.float32([[1,0,x],[0,1,y]])
    dim=(img.shape[1],img.shape[0])
    return cv.warpAffine(img,transMat,dim)

transleted=trans(img,500,500)
# -x ---> shifts to left
#  x ---> shifts to right
#  y ---> shifts to up
# -y ---> shifts to down
cv.imshow('trans',transleted)


# rotation:

def rotate(img,angle,rotPoint=None):
    (height,width)=img.shape[:2]  
    if rotPoint==None:
        rotPoint=(width//2,height//2)
    rotMat=cv.getRotationMatrix2D(rotPoint,angle,1.0)
    dim=(width,height)
    return cv.warpAffine(img,rotMat,dim)

rot=rotate(img,-45)
cv.imshow('rotate',rot)

rot_rot=rotate(rot,-45)
cv.imshow('rot rot',rot_rot)
cv.waitKey(0)
