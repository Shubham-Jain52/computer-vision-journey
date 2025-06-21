import cv2 as cv

def rescale(frame, scale=0.75):
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)
    dim=(width,height)

    return cv.resize(frame, dim, interpolation=cv.INTER_AREA)


vid=cv.VideoCapture(0) #used to capture video from computerweb cam.

while True:
    isTrue, frame= vid.read()          
    frame_resize=rescale(frame)
    cv.imshow('video',frame)
    cv.imshow('video_resized',frame_resize)
    if cv.waitKey(20) & 0xFF==ord('a'):     
        break

vid.release()
cv.destroyAllWindows()
