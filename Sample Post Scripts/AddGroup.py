import requests, json


POST_URL = "http://localhost:8000/index/addgroup/"


dat = {"user": 1, "group": 2}

r = requests.post(POST_URL, params=dat)

print(r.json())

