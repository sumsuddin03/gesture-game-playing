import cv2
import handTrackingmodule as htm
from cvzone import HandTrackingModule as htm2
import mediapipe as mp
from pynput.keyboard import Controller,Key
import time

#setting the controls
wcam,hcam = 640,480
keyboard = Controller()
cap = cv2.VideoCapture(0)

#initializing detector-->you can use any one
detector = htm.handDetector(maxHands=2, detectionCon=0,trackCon=0)
det = htm2.HandDetector(maxHands=2,detectionCon=0.5,minTrackCon=0.5)

while True:

    #read the camera feed
    suc , img = cap.read()

    #detect the hands
    hands,img = det.findHands(img,draw=True,flipType=True)

    #check if there are any hands on screen
    if hands:
        #press the key depending on the state of hands
        if len(hands)==2:
            hand1 = hands[0]
            hand2 = hands[1]
            if hand1['type']=='Left' and det.fingersUp(hand1).count(0)==5:
                keyboard.press(Key.left)
            if hand2['type']=='Right' and det.fingersUp(hand2).count(0)==5:
                keyboard.press(Key.right)
        if len(hands)==1:
            hand = hands[0]
            if hand['type']=='Left' and det.fingersUp(hand).count(0)==5:
                keyboard.press(Key.left)
            if hand['type']=='Right' and det.fingersUp(hand).count(0)==5:
                keyboard.press(Key.right)

    cv2.imshow("video",img)

    if cv2.waitKey(1)==ord('l'):
        break
