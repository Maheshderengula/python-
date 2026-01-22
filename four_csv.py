import csv 
def save_users(filename, users):
    with open(filename,"w" ,newline="") as f:
        writer =csv.writer(f)
        writer.writerow(["id","name"])
        writer.writerows(users)


users = [
    [1,"raju"],
    [2,"soniya"]
]

save_users("four.csv",users)