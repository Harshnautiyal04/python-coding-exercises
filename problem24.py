# get two number and operator from the user to perform arti=himetic operations

num = int(input("Enter 1st number : "))
num1 = int(input("Enter 2nd number : "))
op = input("Enter arthimetic operator : ")

if op == "+":
    print(num+num1)
elif op == "-":
    print(num-num1)
elif op == "*":
    print(num*num1)
elif op == "/":
    if num1 == 0:
        print("zero division error")
    else:
        print("Take another number instead of zero")
else:
    print("The operations is not valid, you are restricted to using this function.")