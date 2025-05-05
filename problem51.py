# take 2 date from the user and find the number of days between them 

# import datetime
# date1 = input("Enter date1 MM-DD-YYY : ")
# date2 = input("Enter date2 MM-DD-YYYY : ")

# date_format = "%m-%d-%Y"

# d1 = datetime.datetime.strptime(date1,date_format)
# d2 = datetime.datetime.strptime(date2,date_format)

# diff = d2-d1

# print(f"The diffrence between {d1.date()} and {d2.date()} is ",diff.days)

# take two date from the user and find number of hours between them
from datetime import datetime

# Take input from user
date1 = input("Enter first date and time (MM-DD-YYYY HH:MM): ")
date2 = input("Enter second date and time (MM-DD-YYYY HH:MM): ")

# Define format including time
date_format = "%m-%d-%Y %H:%M"

# Convert strings to datetime objects
d1 = datetime.strptime(date1, date_format)
d2 = datetime.strptime(date2, date_format)

# Calculate time difference
diff = d2 - d1

# Convert total seconds to hours
hours = diff.total_seconds() / 3600

print(f"Difference between the two dates is: {hours} hours")
