import cvzone
import numpy as np
from cvzone.HandTrackingModule import HandDetector
import cv2



def draw(img,info,prev_pos,canvas):
    fingers,lmList = info
    current_pos = None
    if fingers == [0,1,0,0,0] :
        current_pos = lmList [8][0:2]
        if prev_pos is None:
            prev_pos = current_pos
        cv2.line(canvas,current_pos,prev_pos,(255,0,255),10)
        
    elif fingers == [1,1,1,1,1]:
       canvas = np.zeros_like(img) 
    return current_pos,canvas