import pymongo
try:
    #establish db connection
    client=pymongo.MongoClient('mongodb://localhost:27017/') 
    #get db instance
    db=client['mb']
    #get collection instance
    emp_col=db['employees']
    employees=[
        {'eid':102,'ename':'Sonia','esal':55000},
        {'eid':103,'ename':'Priya','esal':65000},
        {'eid':104,'ename':'Modi','esal':75000},
        {'eid':105,'ename':'Amith','esal':85000},
        {'eid':106,'ename':'Rajni','esal':95000},
    ]
    emp_col.insert_many(employees)
    print("Documents inserted successfully")

except pymongo.errors.PyMongoError as err:
    print(err)