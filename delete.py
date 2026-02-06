import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["mb"]
collection = db["employees"]

result = collection.delete_one({"eid": 101})

print(result.deleted_count, "document deleted")
