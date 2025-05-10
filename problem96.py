#write a python program to find middle element of list item 

num = int(input("Enter number of elements: "))

lst = []

for i in range(num):
    lst.append(int(input(f"Enter number {i+1}: ")))

l = len(lst)

if l == 0:
    print("The list is empty. No middle element.")
elif l % 2 == 1:
    middle_index = l // 2
    print("The middle element of the list is:", lst[middle_index])
else:
    middle1 = lst[l//2 - 1]
    middle2 = lst[l//2]
    print("The list has even number of elements.")
    print("The two middle elements are:", middle1, "and", middle2)
