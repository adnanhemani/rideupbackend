import requests, json


POST_URL = "http://localhost:8000/index/groups/"


dat = {"user": 0}

r = requests.post(POST_URL, params=dat)

print(r.json())

