import requests, json


POST_URL = "http://localhost:8000/index/register/"


dat = {"fname": "Baahil", "lname": "Hemani", "phone_number": "0", "email": "abc@g.com", "driver": False, "own_car": False, "pw": "aahilh", "g": 2}

r = requests.post(POST_URL, params=dat)

print(r.json())

