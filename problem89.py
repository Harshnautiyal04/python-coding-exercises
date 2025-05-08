#write a python program to get age of 10  students from user and store in a list.Condition is that, System should display age that greater than 14 year and less than 20 year

# num = int(input("Enter number : ")) 

# std_age = []

# for i in range(num):
#     std_age.append(int(input("Enter age to store in a list : ")))


# for i in std_age:
#     if i >=14 and i <=20:
#         print("Those whom age is greater than 14 and less 20 is ",i)
#     else:
#         print("The age is not greater than 14 and not less than 20 is ",i)


# write a python program to get name of diffrent students from user and store in a list condition is that system should stored the name of student that start fromm a char 'a' and end at 'a' char

num = int(input("Enter number : "))

std_name = []
updated_lst = []
for i in range(num):
    std_name.append(input("Enter students name to store in a list : "))

for i in std_name:
    if (i.startswith('a')) and (i.endswith('a')):
        updated_lst.append(i)
        print(updated_lst)
    else:
        print("The name is not starts with and ends with a.")