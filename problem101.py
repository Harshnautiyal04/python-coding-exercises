#write a python program to sort students name in ascending order in list and student should display which contain only 5 character

# lst = []

# for i in range(6):
#     lst.append(input("Enter name to store in a list: ")) 

# lst.sort()

# for i in lst:
#     if (len(i) == 5):
#         print(i)


# write a python program to sort students name in desecnding order in list and put A.the end of everu studeent name

lst = []

for i in range(6):
    lst.append(input("Enter name to store in a list : "))

lst.sort(reverse = True)


std_with_suffex = [name + "A" for name in lst]

print(std_with_suffex)