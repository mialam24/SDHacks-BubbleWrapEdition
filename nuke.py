from pymongo import MongoClient

client = MongoClient()
db = client.test
fridge = db.fridge

fridge.delete_many({})
