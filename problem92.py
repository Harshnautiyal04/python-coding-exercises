#Write a python program to find acceleration of an object having velocity v in t time 

# take input time and velocity from user 

u = float(input("Initial velocity (in m/s): "))


v= float(input("Final velocity (in m/s): "))

t = float(input("Enter time (in s): "))

if t == 0:
    print("Print time cannot be zero.")
else:
    acceleration = (u-v)/t
    print(f"The Acceleration is {acceleration} m/s².")