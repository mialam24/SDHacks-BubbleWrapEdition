import cv2
import sys
import os
import time
import numpy as np
import mss

top = 630
left = 70
width = 700
height = 450

sct = mss.mss()

def takePicture(name=None, capture_id=0):
	raw_img = np.array(sct.grab({'top': top,'left': left, 'width': width, 'height': height}))
	raw_img = np.array(raw_img)[:,:, 0:3]
	return raw_img


def main():
    # takePicture(name="one.jpg")
	dirname = 'raw_data' 

	capture_id = int(sys.argv[1])
	base_name = str(sys.argv[2])
	num_shots = int(sys.argv[3])
	fps = float(sys.argv[4])
	
	for i in range(num_shots):
		name = base_name + '_' + str(i) + '.jpg'
		img=takePicture(os.path.join(dirname,base_name,name),capture_id=capture_id)
		cv2.imwrite(os.path.join(dirname,base_name,name),img)
		time.sleep(0.03)
		

if __name__ == '__main__':
    main()
