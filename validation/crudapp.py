#This is a seperate python programme to check the functionalities of APIs

#We run this with different functional calls to perform CRUD functionalities
#This app is linked to crudapi app


import requests
import json

URL = "http://127.0.0.1:8000/studentapi/"

def get_data(id=None):
    data={}
    if id is not None:
        data={'id':id}
    json_data = json.dumps(data)
    r=requests.get(url=URL,data = json_data)
    data=r.json()
    print(data)

# get_data(5)

def post_data():
    data ={
        'name':'Sachin',
        'roll':30,
        'city':'Ranchi'
    }
    json_data = json.dumps(data)
    r=requests.post(url=URL,data=json_data)
    data =r.json()
    print(data)

post_data()

def update_data():
    data = {
        'id':1,
        'name':'Raj',
        'roll':1132

    }
    json_data = json.dumps(data)
    r=requests.put(url = URL,data=json_data)
    data =r.json()
    print(data)

# update_data()

def delete_data():
    data = {
        'id':4
        }
    json_data = json.dumps(data)
    r=requests.delete(url = URL,data=json_data)
    data =r.json()
    print(data)

# delete_data()