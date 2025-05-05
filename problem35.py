# write a python program to get 10 name of the students from the user in a list and display that students name in descending order.

student = []

num = int(input("Enter a number : "))

for i in range(num):
    student.append(input("Enter name of student : "))

print("Original order.")
print(student)

student.sort(reverse=True)

print("Desending order")
print(student)