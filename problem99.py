#write a python program to add number from list that are greater than 5 and less than 10 
# s=0
# num = int(input("Enter number : "))

# lst = []

# for i in range(num):
#     lst.append(int(input("Enter number to store in a list: ")))

# for i in lst:
#     if i>5 and i<10:
#         s+=i

# print(f"The sum is {s}.")

# write a python program to add even number from the list 
num = int(input("Enter number : "))


s = 0


lst = []

for i in range(num):
    lst.append(int(input("Enter number to store in a list : ")))

for i in lst: 
    if i % 2 == 0:
        s+=i

print(f"The sum of even number is {s}.")