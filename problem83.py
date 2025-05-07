# write a program to get name from a list that starts from 'f'

# num = int(input("Enter number : "))

# lst = []

# for i in range(num ):
#     lst.append(input("Enter name to store in a list : ").lower())

# for i in lst:
#     if (i.startswith('f')):
#         print(i)

# write a program to get name from a list that ends at 'f'

num = int(input("Enter number : "))

lst = []

for i in range(num ):
    lst.append(input("Enter name to store in a list : ").lower())

for i in lst:
    if (i.endswith('f')):
        print(i)