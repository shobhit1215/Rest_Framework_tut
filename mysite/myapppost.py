import requests
import json

URL = "http://127.0.0.1:8000/stucreate/"
#Data is in python
data={
    'name':'Sonam',
    'roll':101,
    'city':'Ranchi'
}
#Convert in jason
jason_data = json.dumps(data)
r=requests.post(url = URL,data=jason_data)
data=r.json()
print(data)