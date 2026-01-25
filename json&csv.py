"""
import json 
import csv

#read json file 
with open ("usersy.json","r") as jf:
    data = json.load (jf)

#write to csv file 
with open ("usersy.csv","w", newline ="") as cf:
        writer = csv.dicwrite (cf,filednmaes=data[0].key())
        writer .writeheader()
        writer .writerows(data)

print("json converted to csv successfully")

"""
import requests
import csv

url = "https://dummyjson.com/users"
response = requests.get(url)

users = response.json()["users"]

with open("usersy.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=users[0].keys())
    writer.writeheader()
    writer.writerows(users)

print("✅ API JSON saved as CSV")
