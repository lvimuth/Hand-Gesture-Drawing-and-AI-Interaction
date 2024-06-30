import numpy as np
from cvzone.HandTrackingModule import HandDetector
import cv2
import google.generativeai as genai
import streamlit as st
from draw import draw as draw
from sendToAI import sendToAI as sendToAI

st.set_page_config(layout="wide")

col1,col2=st.columns([2,1])
with col1:
    run = st.checkbox('Run', value=True)
    FRAME_WINDOW = st.image([])
    
with col2:
    st.title("Answer")
    output_text_area = st.subheader("")

cap = cv2.VideoCapture(0)
cap.set(3,1920)
cap.set(4,1080)
prev_pos = None
canvas = None
image_combine = None
output_text = ""
# Initialize the HandDetector class with the given parameters
detector = HandDetector(staticMode=False, maxHands=1, modelComplexity=1, detectionCon=0.5, minTrackCon=0.5)
genai.configure(api_key="AIzaSyD7ViPV0w1dnXdXtYIao7331LM5hlMzbsc")
model = genai.GenerativeModel('gemini-1.5-flash')

def getHandInfo(img):
    hands, img = detector.findHands(img, draw=False, flipType=True)

    # Check if any hands are detected
    if hands:
        # Information for the first hand detected
        hand = hands[0]  # Get the first hand detected
        lmList = hand["lmList"]  
        fingers = detector.fingersUp(hand)
        return fingers,lmList
    else:
        return None
    
while True:

    success, img = cap.read()
    img = cv2.flip(img,1)
    
    if canvas is None:
        canvas =np.zeros_like(img)
        

    info = getHandInfo(img)
    if info:
        fingers,lmList = info
        #print(fingers)
        prev_pos,canvas = draw(img,info,prev_pos,canvas)
        output_text=sendToAI(model,canvas,fingers)
        
    image_combine = cv2.addWeighted(img,0.7,canvas,0.3,0)
    
    # cv2.imshow("Image", img)
    # cv2.imshow("Canvas", canvas)
    # cv2.imshow("Canvas Combined", image_combine)
    FRAME_WINDOW.image(image_combine,channels="BGR")   
    
    if output_text:
        output_text_area.text(output_text)
    cv2.waitKey(1)