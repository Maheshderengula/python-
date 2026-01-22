def get_male_employees(employees):
    return [e["name"] for e in employees if e["gender"] == "M"]

for name in get_male_employees(employees):
    print(name)
