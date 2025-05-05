# write a python program to check its leap year or not
# year = int(input("Enter year : "))

# if (year % 4 == 0 and year%100 != 0) or year % 400 == 0:
#     print("leap year")
# else:
#     print("Not a leap year")

# get 5 year from user in array and print a leap year from the array 

import array as arr

a = arr.array('i',[])

for i in range(5):
    a.append(int(input("Enter your year to store in array = ")))
    print(a[i])


for year in a:
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        print("{} is a leap year.".format(year))
    else:
        print("{} is not a leap year.".format(year))