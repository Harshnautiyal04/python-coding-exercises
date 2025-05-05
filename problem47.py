#get 5 marks from the user store them into array and also get student name. find total and display.each subject marks

# import array as arr

# user  = input("Enter username : ")

# a=arr.array('i',[])
# print("Enter subject marks in order English,Ai,Physics,Computer,Math: ")
# for  i in range(5):
#     a.append(int(input("Enter subjects marks : ")))
# total = 0 

# for i in range(5):
#     total+=a[i]

# print("Hi {}!".format(user))

# print("Your marks is {}.".format(total))
# print("See  your all subject marks!")
# print("English = {}.".format(a[0]))
# print("Ai = {}.".format(a[1]))
# print("Physics = {}.".format(a[2]))
# print("Computer = {}.".format(a[3]))
# print("Math = {}.".format(a[4]))

# get 5 subject and marks and store in an array and display total and average

import array as arr

user = input("Enter username = ")

a = arr.array('i',[])

print("Enter subject marks in order English,Ai,Physics,Computer,Math.")

for i in range(5):
    a.append(int(input("Enter subject marks : ")))
total = 0 

for i in range(5):
    total +=a[i]

avg = total/5

print(f"Hi {user}!")
print(f"Your marks is {total}.")
print("See  your all subject marks!")
print(f"English = {a[0]}.")
print(f"Ai = {a[1]}.")
print(f"Physics = {a[2]}.")
print(f"Computer = {a[3]}.")
print(f"Math = {a[4]}.")
print(f"Your average marks is {avg}.")

