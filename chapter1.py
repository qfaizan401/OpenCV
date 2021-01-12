#Chapter 1: Read- Images, Videos, Webcam

import cv2
import numpy as np
print('Package Imported', cv2.__version__)

#Part 1: Read Images
img_path = 'Resources/lena.jpg'
img = cv2.imread(img_path)
cv2.imshow('Lena', img)
cv2.waitKey(0)

#Part 2: Read Video
video_path = 'Resources/IMG_0275.MOV.mp4'
cap = cv2.VideoCapture(video_path)
    #As we know that video is a squence of images(frames) so we need to loop through it.
while True:
    sucess, img = cap.read()
    print(np.shape(img))
    cv2.imshow('Video', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

#Part 3: Access the WebCam (Very much similar to Read Video)
WebCam_cap = cv2.VideoCapture(0)
    #As we know that video is a squence of images(frames) so we need to loop through it.
while True:
    sucess, img = WebCam_cap.read()
    print(np.shape(img))
    cv2.imshow('Video', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break