def is_even(n):
    return n % 2==0

num = int (input("enter number:"))

if is_even(num):
    print ("even")

else:
    print("odd")