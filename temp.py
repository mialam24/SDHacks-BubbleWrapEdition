import numpy as np
import cv2
import mss
import sys

top = int(sys.argv[1])
left = int(sys.argv[2])
width = int(sys.argv[3])
height = int(sys.argv[4])
sct = mss.mss()

while True:
	raw_img = np.array(sct.grab({'top': top,'left': left, 'width': width, 'height': height}))
	raw_img = raw_img[:,:, 0:3]
	cv2.imshow('hello', raw_img)
	if cv2.waitKey(25) & 0xFF == ord('q'):
		break
