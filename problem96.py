#write a python program to find middle element of list item 

num = int(input("Enter number : "))

lst = []


for i in range(num):
    lst.append(int(input("Enter number to store in a list : ")))

l = len(lst)

half = l/2

middle_elmt = int(half)

print("The middle element of a list is =",middle_elmt)