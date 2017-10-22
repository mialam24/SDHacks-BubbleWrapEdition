from pymongo import MongoClient
from datetime import datetime, timedelta

client = MongoClient()
db = client.test
fridge = db.fridge

def sendText(message):
    print(message)


# Warn if things are close to expiring
# Can set threshold

def checkExp():
    EXPIRATION_THRESHOLD = 8 #days
    items = fridge.find({})
    
    expired = []
    for item in items:
        if datetime.strptime(item['dateExp'],'%Y-%m-%d %H:%M:%S.%f') - datetime.utcnow() > timedelta(days=EXPIRATION_THRESHOLD):
           expired.append(item['name'])
    
    for item in expired:
        sendText("Your {} are going to go bad in {} days!! Eat them soon!!".format(item,EXPIRATION_THRESHOLD))


# Warn if things are almost out
# Can set threshold

# Warn if things are too much
# Can set threshold

# Can check if item is in fridge or not
def has(item):
    item = fridge.find_one({'label':item})
    if item is not None:
        return True
    else:
        return False

# Check when particular item is expiring

# Get all info on particular item

# Get all of the same label

def main():
#	print(has('apple'))
#	print(has('beer'))
	checkExp()

if __name__ == '__main__':
	main()
