
emp = {"eid": 101,
"ename": "Amitabh",
"gender": "M"}

# add new key-value
emp["salary"] = 60000
emp["city"] = "Mumbai"
# update exisiting value
emp["salary"] = 75000
emp["salary"] = 60000
emp["city"] = "Mumbai"
# remove data
emp.pop("city")


print(emp)

#check key exists
if "gender"in emp:
    print("gender exists")


