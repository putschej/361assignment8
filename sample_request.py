# Jennifer Putsche
# putschej@oregonstate.edu
# CS361 Spring 2025
# S2.6 - Assignment 8: "Microservice A"
# See docs for requests: https://docs.python-requests.org/en/latest/user/quickstart/

import requests
import pprint

url = "http://localhost:5000/getTeamRoster"

print("Good request: Jersey number order")
payload = {
    "team name": "DAL",
    "alphabetical order": False
}
response = requests.post(url, json=payload)
pprint.pprint(response.json())

print("Good request: alphabetical order by name")
payload = {
    "team name": "DAL",
    "alphabetical order": True
}
response = requests.post(url, json=payload)
pprint.pprint(response.json())

print("Bad request: team doesn't exist")
payload = {
    "team name": "XYZ",
    "alphabetical order": False
}
response = requests.post(url, json=payload)
pprint.pprint(response.json())
