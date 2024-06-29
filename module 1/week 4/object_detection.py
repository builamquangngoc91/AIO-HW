import cv2
import numpy as np
from PIL import Image
import streamlit as st

MODEL = "model/MobileNetSSD_deploy.caffemodel"
PROTOTXT = "model/MobileNetSSD_deploy.prototxt.txt"

def process_image(image):
    blob = cv2.dnn.blobFromImage(
        cv2.resize(image, (300, 300)), 0.007843, (300, 300), 127.5
    )
    net = cv2.dnn.readNetFromCaffe(PROTOTXT, MODEL)
    net.setInput(blob)
    detections = net.forward()
    return detections

def annotate_image(image, detections, confidence_threshold=0.5):
    # Loop over the detections
    for i in range(detections.shape[2]):
        confidence = detections[0, 0, i, 2]
        
        if confidence > confidence_threshold:
            # Extract the index of the class label from the detections
            idx = int(detections[0, 0, i, 1])
            
            # Extract the (x, y)-coordinates of the bounding box for the object
            box = detections[0, 0, i, 3:7] * np.array([image.shape[1], image.shape[0], image.shape[1], image.shape[0]])
            (startX, startY, endX, endY) = box.astype("int")
            
            # Draw the bounding box around the detected object
            cv2.rectangle(image, (startX, startY), (endX, endY), (0, 255, 0), 2)
    
    return image

st.title('Object Detection')
file = st.file_uploader('Upload an image', type=['jpg', 'jpeg', 'png'])

if file is not None:
    st.image(file)
    image = Image.open(file)
    image = np.array(image)
    detections = process_image(image)
    processed_image = annotate_image(image.copy(), detections)
    st.image(processed_image)