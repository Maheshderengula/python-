import pymongo

try:
    client=pymongo.MongoClient('mongodb://localhost:27017/')
    db=client['mb']
    emp_col=db['employees']
    emp_cursor=emp_col.find()
    employees=list(emp_cursor)
    print(employees)
except pymongo.errors.PyMongoError as err:
    print(err)