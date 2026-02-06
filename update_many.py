import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["mb"]
collection = db["employees"]

result = collection.update_many(
    {"gender": "F"},
    {"$set": {"bonus": 5000}}
)

print(result.modified_count, "documents updated")
