import cv2



def takePicture(name):
	vc = cv2.VideoCapture(0)
	if vc.isOpened(): # try to get the first frame
		rval, frame = vc.read()
		cv2.imwrite(name,frame)
		print("Image captured into " + name)
	else:
		rval = False
		print("Image failed to capture.")

def main():
	takePicture("one.jpg")

if __name__ == '__main__':
	main()
