import cv2

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
    takePicture(capture_id=6)

if __name__ == '__main__':
    main()
