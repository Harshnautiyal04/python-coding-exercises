# get age from the user and convert it into in seconds

age = int(input("Enter your age : "))
print("Age =",age)

age_sec = age*365*24*60*60
age_min = age*365*24*60
age_hour = age*365*24

print("Age convert into sec =",age_sec)
print("Age converted into min =",age_min)
print("Age converted into hour =",age_hour)