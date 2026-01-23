"""
consume REST API
and write users data(uid,name,city,company_name) into new json file
Information about REST API
____________
Usage :Get all users
API URL:https://jsonplaceholder.typicode.com/users
Method Type:GET
Required Fields:None
Access Type:Public

#Extract from rest fromat
import requests
user_resp=requests.get('https://jsonplaceholder.typicode.com/users')
#print (user_resp.__dict__)
usres=user_resp.json()
print(type(usres)) #list

#Transform
new_users=[]

for user in new_users:
    new_users.append({'uid':user['id'],
                      'name':user['username'],
                      'city':user['address']['city'],
                       'company_name':user['company']['name']           
                       })

print(new_users)    
"""
#load 
import json 
fb=open("new_users.json",'w')
json.dump(new_users,fp)
print("New json file created")
fp.close()