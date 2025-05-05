# write a python program get name of week and show holiday if user inputs sunday

# week = input("Enter weekdays : ")

# if week == "sunday" or week == "Sunday" or week == "sun" or week =="Sun":
#     print("It is a Holiday.")
# else:
#     print("It is a Workday.")

# get name of week and show holiday when user inputs sunday or friday

week = input("Enter weekdays : ")


if week == "sunday" or week == "friday" or week == "Sunday" or week == "Friday" or week == "Sun" or week == "Fri" or week =="fri" or week == "sun":
    print("It is a holiday.")
else:
    print("It is a workday.")