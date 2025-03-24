import cv2
import numpy as np
img=cv2.imread('season.jpg')
h,w,channels=img.shape
half=w//2
half2=h//2

top_left=img[:half2,:half]
top_right=img[:half2,half:]
bottom_left=img[half2:,:half]
bottom_right=img[half2:,half:]

cv2.imshow('top left',top_left)
cv2.imshow('top right',top_right)
cv2.imshow('bottom left',bottom_left)
cv2.imshow('bottom right',bottom_right)

cv2.waitKey(0)