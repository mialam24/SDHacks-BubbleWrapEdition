import requests

url = 'http://localhost:3000'
data = { 'name': 'potato', 
		'label': 'apple',
		'dateStored' : 'Today',
		'dateExp' : 'Tomorrow' }

# r = requests.post(url + '/api/in', data=data)
r = requests.get(url + '/api/all')
print(r.json)
