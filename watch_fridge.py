from capture_image import takePicture
from process_image import process_img
from label_image import label_image, init_graph
import liveDiff
import time
import cv2
from multiprocessing import Process
from optical_flow import initializeDirection, direction

from datetime import datetime, timedelta
from pymongo import MongoClient
# import requests
import random

last_added = time.time()

#Connect to local database
client = MongoClient()
db = client.test
fridge = db.fridge

url = 'http://localhost:3000'

def labeller(img):
	cv2.imwrite('temp.jpg', img)
	label = label_image('temp.jpg')
	return label


def differencer(img):
	liveDiff.liveDiff(img)

def addItem(item):
	global last_added

	if time.time() - last_added < 5: return
	now = datetime.utcnow()
	entry = {
             'name': item + ' ' + str(random.randint(0, 1000000)),
             'label': 'tbd',
             'dateStored': str(now),
             'dateExp': now + timedelta(days=7)
	}
	if item == 'apple':
		entry['label'] = item
		delta = timedelta(days=7)
	elif item == 'soda can':
		entry['label'] = item
		delta = timedelta(days=120)
	elif item == 'water bottle':
		entry['label'] = item
		delta = timedelta(days=6000)
	else:
		#print("Error: I don't know")
		return

	entry['dateExp'] = now + delta
	entry['dateExp'] = str(entry['dateExp'])

	print("Adding item", item)
	last_added = time.time()
	fridge.insert_one(entry)

	# r = requests.post(url + '/api/in', data=entry)

def delete():
	fridge.delete_many({})

def watch(rate = 30):
	i = 0
	init_graph()
	img = takePicture()
	old_gray, p0, mask, color = initializeDirection(img)
	masterFrame, masterP = old_gray.copy(), p0
	while(True):
		img = takePicture()
		if i % 15 == 0:
			label = labeller(img)
		differencer(img)
		#cv2.imshow('Raw Image', img)
		movement, old_gray, p0 = direction(old_gray, img, p0, mask, color)
		if movement:
			# print("MOVED")
			addItem(label)
		i += 1
		if cv2.waitKey(25) & 0xFF == ord('q'):
			break

if __name__ == '__main__':
    watch()
	#addItem('apple')
	#delete()
