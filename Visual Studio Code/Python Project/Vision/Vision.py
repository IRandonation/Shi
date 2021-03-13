#coding=utf-8
import cv2 as cv
import numpy as np
import os
import time
import threading

def face_detect_demo(image):
       i=1
       gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
       face_detector = cv.CascadeClassifier("haarcascade_frontalface_default.xml")
       faces = face_detector.detectMultiScale(gray, 1.2, 6)
       global x,y,w,h
       for x, y, w, h in faces:
              cv.rectangle(image, (x, y), (x+w, y+h), (0, 0, 255), 2)
       cv.imshow("result", image)
       clip_image = image[x:x+w,y:y+h]
       cv.imwrite("%d"%i+".jpg",clip_image)
       time.sleep(0.1)
       i = i+1
'''
def face_cut_image(image):
       i = 1
       clip_image = image[x:x+w,y:y+h]
       cv.imwrite("%d"%i+".jpg",clip_image)
       time.sleep(1)
       i = i+1
       print(i)
'''
print("--------- Python OpenCV Tutorial ---------")

capture = cv.VideoCapture(1)
cv.namedWindow("result", cv.WINDOW_AUTOSIZE)

while(True):
       ret, frame = capture.read()
       frame = cv.flip(frame, 1)#左右翻转
       face_detect_demo(frame) 
       c = cv.waitKey(10)
       if c == 27: # ESC
              break
cv.waitKey(0)
cv.destroyAllWindows()