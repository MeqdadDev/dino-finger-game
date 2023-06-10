# pip install pynput
# pip install opencv-python
# pip install mediapipe
# pip install detectors_world

# Dino Game link: https://chromedino.com/

import cv2 as cv
from pynput.keyboard import Key, Controller
from detectors_world import DetectorCreator

cap = cv.VideoCapture(0)

creator = DetectorCreator()

hand = creator.getDetector("hand")

keyboard = Controller()

def check_index_finger(landmarks):
    if len(landmarks) != 0:
        if landmarks[8][2] < 150:
            keyboard.release(Key.down)
            print("UP")
            keyboard.press(Key.up)
        elif landmarks[8][2] > 350:
            keyboard.release(Key.up)
            print("DOWN")
            keyboard.press(Key.down)

while True:
    status, img = cap.read()
    hand.detect(img, drawOnHand=True)

    lms = hand.locate(img, drawOnHand=True, handsNumber=1)
    check_index_finger(lms)

    cv.line(img, (100, 150), (500, 150), (0, 255, 0), 1)
    cv.line(img, (100, 350), (500, 350), (0, 255, 0), 1)
    
    cv.imshow("T-Rex Dino Game", img)
    k = cv.waitKey(1)
    
    # if Esc is pressed -> Exit
    if k % 255 == 27:
        break

# For Python venv problem in Windows (running scripts is disabled on this system)
# `Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy Unrestricted`