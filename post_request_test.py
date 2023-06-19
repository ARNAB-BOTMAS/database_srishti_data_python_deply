import requests

url = 'http://127.0.0.1:5000/users'  # Replace with the actual URL of the API

data = {
    "email": "asdasd",
    "gender": "asdasdasd",
    "id": "1215",
    "name": "aswdasd",
    "password": "asdasdasd"
}  # Replace with the data you want to send in the request body

data = requests.get(url)
datas = data.json()
for person in datas:
    id = person['id']
    name = person['name']
    gender = person['gender']
    password = person['password']
    pack = f"{id},{name},{gender},{password}"
    packs = pack.split(',')
    print(packs)
