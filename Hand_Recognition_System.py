
import cv2

from ML_model import ML_Selector

import HandTracker as ht

wcam,hcam = 640,480
cap = cv2.VideoCapture(0)
cap.set(3,wcam) 
cap.set(5,hcam) 

detector = ht.Hand_Detector()

tips = [4,8,12,16,20]
model = ML_Selector("hands_data.csv")
model.run()

while True:
    success, img = cap.read()
    img = detector.Discover_Hand(img)
    locs = detector.location(img)
    #print(locs)
    
    if len(locs)!=0:
        fingers = []
        
        if locs[tips[0]][1] > locs[tips[0]-1][1]:
            fingers.append(1)
        else:
            fingers.append(0)
            
        for tip in range(1,5):
            if locs[tips[tip]][2] < locs[tips[tip]-2][2]:
                fingers.append(1)
            else:
                fingers.append(0)
        
        val = model.find(fingers)
        if val[0] == 0:
            cv2.putText(img,"Thumbs Up!",(10,70),cv2.FONT_HERSHEY_PLAIN,3,(255,0,255),3)
        elif val[0] == 1:
            cv2.putText(img,"Scissors!",(10,70),cv2.FONT_HERSHEY_PLAIN,3,(0,0,255),3)
        elif val[0] == 2:
            cv2.putText(img,"Paper!",(10,70),cv2.FONT_HERSHEY_PLAIN,3,(255,0,0),3)
        elif val[0] == 3:
            cv2.putText(img,"Rock!",(10,70),cv2.FONT_HERSHEY_PLAIN,3,(0,255,0),3)
        else:
            pass
            
    cv2.imshow("Image",img)
    cv2.waitKey(1)

