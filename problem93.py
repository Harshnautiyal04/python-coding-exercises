#write a python program to find force of a man on a object which mass and acceleration. Get Mass and acceleration from user 
# Formula : F=ma

m = float(input("Enter mass (in kg): "))
a = float(input("Enter acceleration (in m/s²): "))

# F = ma

force = m*a
print(f"Force of a man {force} N.")
