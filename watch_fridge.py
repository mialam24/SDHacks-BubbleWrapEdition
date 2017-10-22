from capture_image import takePicture
from process_image import process_img
from label_image import label_image, init_graph
import liveDiff
import time
import cv2
from multiprocessing import Process

img = None

def labeller():
	global img
	while True:
		cv2.imwrite('temp.jpg', img)
		label = label_image('temp.jpg')


def differencer():
	global img
	while True:
		liveDiff.liveDiff(img)


def watch(rate = 30):
	init_graph()
	global img
	img = takePicture()
	try:
		Process(target=differencer).start()
		Process(target=labeller).start()
	except Exception as e:
		print("Error: unable to start thread")
		print(e)
	
	while(True):
		img = takePicture()
		cv2.imshow('Raw Image', img)
		if cv2.waitKey(25) & 0xFF == ord('q'):
			break

if __name__ == '__main__':
    watch()
