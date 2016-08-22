import requests, json


POST_URL = "http://localhost:8000/index/groupsinfo/"


dat = {"group": 1}

r = requests.post(POST_URL, params=dat)

print(r.json())

