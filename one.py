"""
import csv 
fp = open ('usere.csv','r')
emp_csv =csv.reader(fp)
emp_data = list(emp_csv)

for emp in emp_data[1:]:
    print(emp[1])

fp.close()
"""
import csv 
employees=[
            (101,'rahul','Male'),
            (102,'Sonia','Female'),
            (103,'Priya','Female')
           ]
fp=open('user.csv','w',newline="")

csv_writer=csv.writer(fp)
csv_writer.writerow(['uid','uname','gender'])#csv header
csv_writer.writerows(employees)              #csv data

print('New CSV File Created successfully')