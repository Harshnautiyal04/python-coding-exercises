#write a program to find sum of two number (less than 50 and positive number)

num1 = int(input("Enter 1st number : "))
num2 = int(input("Enter 2nd number : "))

if (num1<50,num2<50)and (num1>0,num2>0):
    print("Addition =",num1+num2)
else:
    print("The number is should not less than zero and greater than 50.")
