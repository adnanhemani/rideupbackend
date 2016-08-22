import requests, json

POST_URL = "http://localhost:8000/index/login/"
dat = {"email": "adnan.h@berkeley.edu", "password": "test12345"}

r = requests.post(POST_URL, params=dat)

#r = requests.get(POST_URL)
print(r.json())