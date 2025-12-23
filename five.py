employees=[
    {'eid':101,'ename':'raju','gender':'M'},
    {'eid':102,'ename':'soniya','gender':'F'},
    {'eid':103,'ename':'priyanka','gender':'F'},
    {'eid':104,'ename':'modi','gender':'M'},
]
gender_map = {"M": "male", "F": "female"}

for emp in employees:
    print(emp["ename"],"=", gender_map[emp["gender"]])
