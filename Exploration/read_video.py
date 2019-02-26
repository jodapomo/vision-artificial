import numpy as np
import cv2
import matplotlib.pyplot as plt


cap = cv2.VideoCapture('res/test1.mp4')

while(cap.isOpened()):
    ret, frame = cap.read()

    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
