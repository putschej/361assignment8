# Jennifer Putsche
# putschej@oregonstate.edu
# CS361 Spring 2025
# S2.6 - Assignment 8: "Microservice A"
# See docs for requests: https://docs.python-requests.org/en/latest/user/quickstart/

import requests
import time
import pprint

url = "http://localhost:5000/getTeamRoster"

print("="*80 + "\nValid request: Jersey number order")
payload = {
    "team name": "DAL",
    "alphabetical order": False
}
print("Sending request with payload:", payload)
response = requests.post(url, json=payload)
time.sleep(5)
print("Response received:")
pprint.pprint(response.json())

print("="*80 + "\nValid request: alphabetical order by name")
payload = {
    "team name": "DAL",
    "alphabetical order": True
}
print("Sending request with payload:", payload)
response = requests.post(url, json=payload)
time.sleep(5)
print("Response received:")
pprint.pprint(response.json())

print("="*80 + "\nInvalid request: team doesn't exist")
payload = {
    "team name": "XYZ",
    "alphabetical order": False
}
print("Sending request with payload:", payload)
response = requests.post(url, json=payload)
time.sleep(5)
print("Response received:")
pprint.pprint(response.json())
