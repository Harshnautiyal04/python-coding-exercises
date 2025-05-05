# write a python program to get 6 subject marks from the user and calculate total and average of that marks and display to the user.

eng = int(input("enter Your first subject marks : "))
sci = int(input("Enter your second subject marks : "))
math = int(input("Enter your third subject marks : "))
IT = int(input("Enter your fourth subject marks : "))
sst  = int(input("enter your fifth subject marks : "))
hindi = int(input("enter your sixth subject marks : "))

total = eng+sci+IT+math+sst+hindi

average = total/6

percentage = (total/600) *100

print("The total marks is {}.".format(total))
print("The average of total marks is {}.".format(average))
print("The percentage is {}.".format(percentage))