import cv2 as cv

# img=cv.imread('image.png')   # using to import the image.
# cv.imshow('dog', img)       # used to show the image.
# cv.waitKey(0)




vid=cv.VideoCapture(0) #used to capture video from computerweb cam.
# vid=cv.VideoCapture('file path') #used to capture video from a perticular file..

while True:
    isTrue, frame= vid.read()          # reads video frame by frame, and then displays it as an image.
    cv.imshow('video',frame)
    if cv.waitKey(20) & 0xFF==ord('a'):     # plays video until the letter "a" is not pressed on the keyboard.
        break

vid.release()
cv.destroyAllWindows()