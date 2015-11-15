import requests
import json


r = requests.get("https://hackbulgaria.com/api/students/")
data = r.json()
with open("hack_api.json", "w") as f:
    json.dump(data, f, indent=True, ensure_ascii=False)
