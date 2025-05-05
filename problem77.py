#write a python program to check if the first and last number of a tuple is the same or not 

# lst = []

# num = int(input("Enter number : "))

# for i in range(num):
#     lst.append(int(input("Enter number to store in a list : ")))

# my_tuple = tuple(lst)


# if my_tuple[0]==my_tuple[-1]:
#     print("The first and last element in a tuple is same.")
# else:
#     print("The first and last element in a tuple is not same.")

#write a python program to store students name in a list and check if the fist character of student first and first character is same last student 

num = int(input("Enter number : "))

lst = []

for i in range(num):
    lst.append(input("Enter name to store in a list : "))

if lst[0][0]==lst[-1][0]:
    print("The first character of last student and first student is same.")
else:
    print("The first character of last and first student is not same.")