#This is a seperate application of python 


import requests
# url for request
URL = "http://127.0.0.1:8000/stulist/"

#place a request
r=requests.get(url = URL)

#parse data to json

data = r.json()
# print data

print(data)