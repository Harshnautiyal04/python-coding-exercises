# get a number from the user and convert into factorial

# 1st method

num = int(input("Enter a number : "))
fact=1

for i in range(1,num+1):
    fact*=i
print(f"Factorial of {num} is",fact)

# 2nd method 

# import math

# num = int(input("Enter a number : "))

# fact = math.factorial(num)

# print(f"Factorial of {num} is",fact)
