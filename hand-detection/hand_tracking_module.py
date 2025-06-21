import cv2 as cv
import mediapipe as mp
import time

class hand_detection():                         
    def __init__(self, mode=False, max_num_hands=2, min_detection_confidence=0.5, min_tracking_confidence=0.5): 
        self.mode = mode
        self.max_num_hands = max_num_hands
        self.min_detection_confidence = min_detection_confidence
        self.min_tracking_confidence = min_tracking_confidence

        self.mp_hands = mp.solutions.hands
        self.mp_draw = mp.solutions.drawing_utils
        self.hands = self.mp_hands.Hands(
            static_image_mode=self.mode,
            max_num_hands=self.max_num_hands,
            min_detection_confidence=self.min_detection_confidence,
            min_tracking_confidence=self.min_tracking_confidence
        )
        self.results = None

    def detection(self, image, draw=True):         
        rgbimg = cv.cvtColor(image, cv.COLOR_BGR2RGB)
        self.results = self.hands.process(rgbimg)

        if self.results.multi_hand_landmarks:      
            for hand_landmarks in self.results.multi_hand_landmarks:      
                if draw:     
                    self.mp_draw.draw_landmarks(image, hand_landmarks, self.mp_hands.HAND_CONNECTIONS)
        return image

    def find_position(self, image, hand_no=0, draw=True):
        landmark_list = []
        if self.results.multi_hand_landmarks:
            my_hand = self.results.multi_hand_landmarks[hand_no]
            h, w, c = image.shape
            for id, lm in enumerate(my_hand.landmark):
                cx, cy = int(lm.x * w), int(lm.y * h)
                cz = int(lm.z * w)  # Approximate Z scaling using image width
                landmark_list.append((id, cx, cy, cz))
                if draw:
                    cv.circle(image, (cx, cy), 7, (0, 255, 0), cv.FILLED)
        return landmark_list


def main():
    vid = cv.VideoCapture(0)
    currentTime = 0
    previousTime = 0
    detector = hand_detection()

    while True:
        isTrue, frame = vid.read()
        frame = cv.flip(frame,1)
        image = detector.detection(frame)
        landmarks = detector.find_position(image)

        if landmarks:
            # Print index finger tip with Z coordinate
            print("Index Finger Tip:", landmarks[8])  # (id, x, y, z)

        currentTime = time.time()
        fps = 1 / (currentTime - previousTime)
        previousTime = currentTime

        cv.putText(image, str(int(fps)), (10, 70), cv.FONT_HERSHEY_DUPLEX, 3, (25, 7, 5))
        cv.imshow('cam feed', image)

        if cv.waitKey(20) & 0xFF == ord('d'):
            break

    vid.release()
    cv.destroyAllWindows()


if __name__ == "__main__":
    main()
