
import csv

# Reading from CSV file
with open("user.csv", mode="r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
