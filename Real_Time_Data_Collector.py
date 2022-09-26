
import cv2
import HandTracker as ht
import time
import csv

wcam,hcam = 640,480
cap = cv2.VideoCapture(0)
cap.set(3,wcam) 
cap.set(5,hcam) 

detector = ht.Hand_Detector()
tips = [4,8,12,16,20]

main = []
names = ['thumbsup','scissors','paper','rock']
for i in names:
    for j in range(400):
        
        success, img = cap.read()
        img = detector.Discover_Hand(img)
        locs = detector.location(img)
        if len(locs)!=0:
            fingers = []
            
            cv2.putText(img,f"Show {i}",(10,70),cv2.FONT_HERSHEY_PLAIN,3,(255,0,255),3)
            if locs[tips[0]][1] > locs[tips[0]-1][1]:
                fingers.append(1)
            else:
                fingers.append(0)
                    
            for tip in range(1,5):
                if locs[tips[tip]][2] < locs[tips[tip]-2][2]:
                    fingers.append(1)
                else:
                    fingers.append(0)
            main.append(fingers+[i])
    
    
        cv2.imshow("Image",img)
        cv2.waitKey(1)
    time.sleep(3)
    
fields = ['thumb','index','middle','ring','little','result']
filename = "hands_data.csv"
with open(filename, 'w+',newline="") as csvfile: 
    csvwriter = csv.writer(csvfile) 
    csvwriter.writerow(fields) 
    csvwriter.writerows(main)
    
print("\n\nData Collection is successfully Completed!!\n\n")
cv2.destroyAllWindows()