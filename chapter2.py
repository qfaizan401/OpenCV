#Chapter 2: Basic Functions

import cv2
import numpy as np

img = cv2.imread('Resources/lena.jpg')
kernel = np.ones((5,5), np.uint8)
print(kernel)

GrayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #Convert Color Img to Grayscale
BlurImg = cv2.GaussianBlur(img, (15,15), 0) #Convert Img to Blur Img
CannyImg = cv2.Canny(img, 150, 200) #Look for the edges of the Img
ImgDialation = cv2.dilate(CannyImg, kernel, iterations=1) #When the Img has undectected edges that means the line draw at edges is uncompeleted for that we do Image dialation
ErodedImg = cv2.erode(ImgDialation, kernel, iterations=1) #Opposite of Dialation is called Erodetion

cv2.imshow('Original Image',img)
cv2.imshow('Gray Image',GrayImg)
cv2.imshow('Blur Image',BlurImg)
cv2.imshow('Edge Detection',CannyImg)
cv2.imshow('Image Dialation',ImgDialation)
cv2.imshow('Image Erodetion', ErodedImg)

cv2.waitKey(0)