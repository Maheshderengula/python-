# input statement:


#example 1
name = input ("enter name :")
print("hello",name,sep=',',end=" ")
print("hii")



#example 2:

num = int ( input ("give value of num:"))

print("you entered:",num,sep="")


#example 3:
pi = float(input("pi: "))
print("value of pi:",pi,sep="")


# example 4:
a = input()
x,y,z = a.split(" ")
sum = int(x)+int(y)+int(z)

print(sum)

#example  5 :
#"mahi",25
inp = input("enter name and age:")
name,age = inp.split(",")
print("name:",name,",age: ",age) 