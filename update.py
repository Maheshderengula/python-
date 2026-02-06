import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["company"]
collection = db["employees"]

result = collection.update_one(
    {"eid": 101},                 # condition
    {"$set": {"salary": 45000}}   # new value
)

print(result.modified_count, "document updated")
