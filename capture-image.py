import cv2

def takePicture(name, capture_id=0):
	vc = cv2.VideoCapture(capture_id)
	if vc.isOpened(): # try to get the first frame
		_, frame = vc.read()
		cv2.imwrite(name,frame)
		print("Image captured into " + name)
	else:
		print("Image failed to capture.")

def main():
	# takePicture("one.jpg")
	takePicture("one.jpg", 6)

if __name__ == '__main__':
	main()
