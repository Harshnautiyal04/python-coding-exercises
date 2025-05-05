# write a python program to find the second position of  a student in a list and display marks 
# num = int(input("Enter no of students marks you want : "))

# lst = []

# for i in range(num):
#     lst.append(int(input("Marks obtained by students : ")))

# print(f"Total result of students {lst}.")

# lst.sort(reverse  = True)

# print("The 2nd postion of a student marks  is =",lst[1])

# write a python program to find the second positon of a studnet in a list and display student marks and thier name .
num = int(input("Enter no of studnets marks you want : "))

lst = []

for i in range(num):
    marks = int(input("Marks obtained by students : "))
    name = input("Students who get marks : ")
    lst.append((name,marks))
print("Total marks obtained by each students." )

for name,marks in lst:
    print(f"{name} = {marks} ")

lst.sort(reverse = True)

print(f"The second positon marks is {lst[1]}.") 