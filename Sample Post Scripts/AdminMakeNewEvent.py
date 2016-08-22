import requests, json


POST_URL = "http://localhost:8000/index/adminmakenewevent/"


dat = {"dt_created": "2016-08-16 16:00", "name":"Testing?", "event_time":"2016-08-16 20:00", "signup_expiry": "2016-08-16 19:00", "group": 1, "active": True}

r = requests.post(POST_URL, params=dat)

print(r.json())

