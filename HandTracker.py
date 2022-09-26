import cv2
import mediapipe as mp

class Hand_Detector():
    def __init__(self, mode=False, maxHands=2, detectionCon=0.5, trackCon=0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.trackCon = trackCon        

        self.mphands = mp.solutions.hands
        self.hands = self.mphands.Hands()
        self.mpdraw = mp.solutions.drawing_utils
        
    def Discover_Hand(self,img,start_draw=True):
        
        #imgrgb = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        imgrgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgrgb)
        #print(results.multi_hand_landmarks)
        
        if self.results.multi_hand_landmarks:
            for hand_land in self.results.multi_hand_landmarks:
                if start_draw:
                    self.mpdraw.draw_landmarks(img, hand_land, self.mphands.HAND_CONNECTIONS)
                
        return img
     
    
    def location(self,img,handno=0):
        
        locs = []
        if self.results.multi_hand_landmarks:
            
            myhand = self.results.multi_hand_landmarks[handno]
            
            for ID, lm in enumerate(myhand.landmark):
                h,w,c= img.shape
                cx,cy = int(lm.x*w), int(lm.y*h)
                locs.append([ID,cx,cy])
                
        return locs
    
    
def main():
    
    cap = cv2.VideoCapture(1)
    detector = Hand_Detector()
    d = 'y'
    while d=='y':
        success, img = cap.read()
        img = detector.Discover_Hand(img)
        locs = detector.location(img)
        
        if len(locs)!=0:
            print(locs[4])
        
        cv2.imshow("Image",img)
        cv2.waitKey(1)

if __name__ == '__main__':
    main()