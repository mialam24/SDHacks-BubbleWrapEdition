from flask import Flask, render_template
from pymongo import MongoClient

client = MongoClient()
db = client.test
fridge = db.fridge

app = Flask(__name__)

@app.route('/')
def index():
	entry = {
				'item': "apple",
				'quantity': 3,
				'entryDate': '10/21/2017',
				'expDate': '10/22/2017',
			  }
	entries = [entry]
	entries = fridge.find()
	return render_template('index.html', entries=entries)

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000)
