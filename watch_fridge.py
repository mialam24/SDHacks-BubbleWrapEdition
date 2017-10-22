from capture_image import takePicture

from process_image import process_img
from label_image import label_image, init_graph
import liveDiff
import time
import cv2
from multiprocessing import Process


def labeller(img):
	cv2.imwrite('temp.jpg', img)
	label = label_image('temp.jpg')


def differencer(img):
	liveDiff.liveDiff(img)


def watch(rate = 30):
	i = 0
	init_graph()
	while(True):
		img = takePicture()
		if i % 15 == 0:
			labeller(img)
		differencer(img)
		cv2.imshow('Raw Image', img)
		i += 1
		if cv2.waitKey(25) & 0xFF == ord('q'):
			break

if __name__ == '__main__':
    watch()
