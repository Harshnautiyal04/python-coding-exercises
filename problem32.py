# get  2 number 
#pass the function
# #max

# num = int(input("Enter a number : "))
# num1 = int(input("Enter a number : "))

# def max_num(num,num1):
#     return max(num,num1)

# print("Between {} and {} the greater number is ".format(num,num1),max(num,num1))

#find minimum pass in function between 2 number take input from user

x = int(input("Enter a number : "))
y = int(input("Enter a number : "))

def min_num(a,b):
    print("Finding the minimum number between {} and {}.".format(x,y))
    print("The value of 1st number is {}.".format(x))
    print("The value of 2nd number is {}.".format(y))
    if x<y:
        print("{} is minimum number.".format(x))
    else:
        print("{} is minimum number.".format(y))

min_num(x,y)