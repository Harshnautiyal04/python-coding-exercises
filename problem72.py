#write a python program to shuffle a list of diffrent color code
# import random
# num = int(input("Enter a number : "))

# lst = []

# for i in range(num):
#     lst.append(input("Enter a color : "))

# print("Original List!")

# print(lst)

# print("Shuffled list!")

# random.shuffle(lst)

# print(lst)


# write a python program to store color in a list and print them into descending to ascending order 
num = int(input("Enter the number : "))
lst = []

for i in range(num):
    lst.append(input("Enter color : "))

print("Original list!")
print(lst)

lst.sort(reverse = True)
print("List in descending order!")

print(lst)
