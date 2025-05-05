# write a program which display  numbers that are divisible by 3 from a list 

# num = int(input("Enter number : "))

# lst = []

# for i in range(num):
#     lst.append(int(input("Enter number to store in a list : ")))

# for i in lst:
#     if i%3==0:
#         print(f"Those numbers which are divisible by 3 are = {i}")

# write a program which display  numbers that are divisible by 3 and 5  from a list 

num = int(input("Enter number : "))

lst = []

for i in range(num):
    lst.append(int(input("Enter number to store in a list : ")))

for i in lst:
    if i%3==0 and i%5==0:
        print(f"Those numbers which are divisible by 3 and 5 are = {i}")
