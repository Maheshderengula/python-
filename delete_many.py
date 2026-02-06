import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["mb"]
collection = db["employees"]

result = collection.delete_many({"gender": "M"})

print(result.deleted_count, "documents deleted")
