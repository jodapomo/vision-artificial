import numpy as np
import cv2
import matplotlib.pyplot as plt

img = cv2.imread("res/test0.jpeg")

img_t = cv2.cvtColor(img, cv2.COLOR_BGR2HSV_FULL)

h_component = img_t[:,:,0]
s_component = img_t[:,:,1]
s_component = img_t[:,:,2]

img_r = img_t

plt.imshow(img_r, cmap="hsv") 

plt.show()
