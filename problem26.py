# write a python program for an even or odd 

# num = int(input("Enter a number : "))

# if num%2==0:
#     print("{} is an even number and its square is ".format(num))
# else:
#     print("{} is an odd number and its square is ".format(num))

# write a program for an even or odd no check or its square 

num = int(input("Enter a number : "))

if num%2==0:
    print("{} is an even number and its square is ".format(num),num**2)
else:
    print("{} is an odd number and its square is ".format(num),num**2)