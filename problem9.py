# write a python program to get a number from the user and display table for that number

# num = int(input("Enter a number : "))

# print("The table of {}.".format(num))
# for i in range(1,11):
#     print("{} * {} = ".format(i,num),i*num)

# Write a python  program that take two number from the user and display 2 table from that number

num = int(input("Enter a number : "))
num1 = int(input("Enter a number : "))

print("The table of {}.".format(num))

for i in range(1,11):
    print("{} * {} = ".format(i,num),i*num)

print("The table of {}".format(num1))
for j in range(1,11):
    print("{} * {} = ".format(j,num1),j*num1)



