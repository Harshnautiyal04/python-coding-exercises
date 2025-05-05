# write a pogram to store color ,in the list, and count that color and display to the user
# lst = ['red','green','black','white','blue']

# print(len(lst))

# get element from user save in  lst and print count

num = int(input("Enter number : "))
lst = []

for i in range(num):
    lst.append(input("Enter color : "))
    color = len(lst)
print("The number of color in a list is",color)
