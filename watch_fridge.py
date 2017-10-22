from capture_image import takePicture
from process_image import process_img
from label_image import label_image
import time
import cv2

def watch(rate = 30):
    while(True):
        time.sleep(1/rate)
        img = takePicture()
        cv2.imshow('Raw Image', img)
        proc_img = process_img(img)
        cv2.imshow('Processed Image', proc_img)
		label = label_image(proc_img)
		
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

if __name__ == '__main__':
    watch()
