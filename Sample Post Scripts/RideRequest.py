import requests, json


POST_URL = "https://calm-garden-29993.herokuapp.com/index/requestride/"


dat = {"user": 1, "driver_leaving_time": "7:29", "driver_spaces": 2, "special_requests": None, "event_id": 1}

new_dat = {"user": 1, "driver_leaving_time": "None", "driver_spaces": 0, "special_requests": "None", "event_id": 1}

r = requests.post(POST_URL, params=new_dat)

print(r.json())

