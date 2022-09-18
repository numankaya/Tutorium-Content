import cv2
import mediapipe

camera = cv2.VideoCapture(0)
mpHands = mediapipe.solutions.hands
mpDraw = mediapipe.solutions.drawing_utils

hands = mpHands.Hands()
while True:
    success, img = camera.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    hlms = hands.process(imgRGB)
    print(hlms.multi_hand_landmarks)
    if hlms.multi_hand_landmarks:
        for handlandmarks in hlms.multi_hand_landmarks:
            mpDraw.draw_landmarks(img, handlandmarks, mpHands.HAND_CONNECTIONS)
    cv2.imshow("Camera",img)
    if cv2.waitKey(1) & 0xFF == ord("x"):
        break