#Write a python program to find acceleration of an object having velocity v in t time 

# take input time and velocity from user 

# u = float(input("Initial velocity (in m/s): "))


# v= float(input("Final velocity (in m/s): "))

# t = float(input("Enter time (in s): "))

# if t == 0:
#     print(Time cannot be zero.")
# else:
#     acceleration = (u-v)/t
#     print(f"The Acceleration is {acceleration} m/s².")

# write a python program to find time taken by an object having velocity diffrence 'dv' and 'a' acceleration. Get velocity and acceleration from the user.


u = float(input("Initial velocity (in m/s): "))


v= float(input("Final velocity (in m/s): "))

a = float(input("Enter acceleration (in m/s²): "))

dv = u-v

if a == 0:
    print("Acceleration cannot be zero.")
else:
    t= dv/a
    print(f"The time is {t} s.")