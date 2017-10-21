import cv2
import sys
import os

def takePicture(name=None, capture_id=0):
    vc = cv2.VideoCapture(capture_id)
    if vc.isOpened(): # try to get the first frame
        _, frame = vc.read()
        cv2.imwrite(name,frame)
        print("Image captured into " + name)
        return frame
    else:
        print("Image failed to capture.")
        return None

def main():
    # takePicture(name="one.jpg")
	dirname = 'raw_data' 

	capture_id = int(sys.argv[1])
	base_name = str(sys.argv[2])
	num_shots = int(sys.argv[3])
	
	for i in range(num_shots):
		name = base_name + '_' + str(i) + '.jpg'
		takePicture(os.path.join(dirname,base_name,name),capture_id=capture_id)
		

if __name__ == '__main__':
    main()
