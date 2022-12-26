#This code demonstrate how to show location of hand landmark
import cv2
import mediapipe as mp
import numpy as np

Nfing = 5
cap = cv2.VideoCapture(0)

#Call hand pipe line module
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils


arr = np.zeros((21, 2))

while True:
    fing = []
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    #print(results.multi_hand_landmarks)
    
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x*w), int(lm.y*h)
                arr[id] = [cx, cy]
                #print(id , arr[id])
                #print(arr[12, 1], arr[11, 1])
            if arr[4, 0] < arr[3, 0]:
                #Nfing = 1
                fing.append("Thumbs finger")
            if arr[8, 1] < arr[7, 1]:
                #Nfing = 1
                fing.append("Index finger")
            if arr[12, 1] < arr[11, 1]:
                fing.append("Middle finger")
            if arr[16, 1] < arr[15, 1]:
                fing.append("Ring finger")
            if arr[20, 1] < arr[19, 1]:
                fing.append("Pinky finger")
            # if cx[4] > cx[3]:
            #     Nfing = 4
            # else:
            #     Nfing = 5


            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)
    Nfing = len(fing)
    cv2.putText(img, str(Nfing), (10, 150), cv2.FONT_HERSHEY_PLAIN, 1.5,
                (252, 65, 3), 3)
    cv2.putText(img, str(fing), (10, 70), cv2.FONT_HERSHEY_PLAIN, 1.5,
                (252, 65, 3), 3)
    cv2.imshow("Image", img)
    cv2.waitKey(1)
#Closeing all open windows
#cv2.destroyAllWindows()