from capture_image import takePicture
from process_image import process_img
from label_image import label_image, init_graph
import liveDiff
import time
import cv2
from multiprocessing import Process
from optical_flow import initializeDirection, direction

def labeller(img):
	cv2.imwrite('temp.jpg', img)
	label = label_image('temp.jpg')


def differencer(img):
	liveDiff.liveDiff(img)


def watch(rate = 30):
	i = 0
	init_graph()
	img = takePicture()
	old_gray, p0, mask, color = initializeDirection(img)
	masterFrame, masterP = old_gray.copy(), p0
	while(True):
		img = takePicture()
		if i % 15 == 0:
			labeller(img)
		differencer(img)
		#cv2.imshow('Raw Image', img)
		movement, old_gray, p0 = direction(old_gray, img, p0, mask, color)
		if movement:
			print("MOVED")
		i += 1
		if cv2.waitKey(25) & 0xFF == ord('q'):
			break

if __name__ == '__main__':
    watch()
