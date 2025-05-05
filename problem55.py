# write a python program to show the current date on the  user request 

# from datetime import datetime

# user = input("Do you want to get current date and time? (yes/no) : ")

# if user == "yes" or "Yes":
#     print(datetime.now().date())
# elif user == "no" or "No":
#     print("Okay we did not display current date.")
# else:
#     print("Plz enter only yes or no.")

# convert current date into miliseconds

from datetime import datetime

now= datetime.now()

time_stamp = now.timestamp()

milisec = int(time_stamp*1000)

print(f"Current date  is {now.date()} and milisec is {milisec}.")