import cv2 as cv
import mediapipe as mp
import time



vid=cv.VideoCapture(0)


mp_hands=mp.solutions.hands
mp_draw=mp.solutions.drawing_utils

hands=mp_hands.Hands(
    max_num_hands=2,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)

currentTime=0
previousTime=0
while True:
    isTrue, image=vid.read()
    image=cv.flip(image,1)     # gives mirror image.
    rgbimg=cv.cvtColor(image,cv.COLOR_BGR2RGB)
    result=hands.process(rgbimg)        # process the frame of the video and then detects hands and landmarks.

    if result.multi_hand_landmarks:      # if hands exist in the frame then
        for hand_landmarks in result.multi_hand_landmarks:      # get exact coordinates of thoes hands from the results.
            mp_draw.draw_landmarks(image,hand_landmarks,mp_hands.HAND_CONNECTIONS)    # displays all the connections
           
            for id, landmark in enumerate(hand_landmarks.landmark):      #each hand point has a ID and so each id has different coordinate.
                w,h,c=image.shape
                cx=(int(landmark.x*w))
                cy=(int(landmark.y*h))
                print(f'id ={id} ,x={cx} ,y={cy}')     # prints coordinate for all the 21 point on the hand.
    currentTime=time.time()
    fps=1/(currentTime-previousTime)
    previousTime=currentTime

    cv.putText(image,str(int(fps)),(10,70),cv.FONT_HERSHEY_DUPLEX,3,(25,7,5))
    
    
    cv.imshow('cam feed',image)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

vid.release()
cv.destroyAllWindows()
