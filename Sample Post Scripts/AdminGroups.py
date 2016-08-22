import requests, json


POST_URL = "http://localhost:8000/index/admingroups/"


dat = {"user": 0}

r = requests.post(POST_URL, params=dat)

print(r.json())

