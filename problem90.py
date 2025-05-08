# write a python program find a density of an obeject 

# first we take input mass from user and then volume 

# density formula is mass/volume 

# mass = float(input("Enter mass (in grams): "))

# volume = float(input("Enter volume (in cm³): "))

# #calculate density

# if volume == 0:
#     print("Volume cannot be zero.")
# else:
#     density = mass/volume
#     print(f"Densisty is {density} g/cm³ .")

# write a python program to find a masss of an object through density

density = float(input("Enter density (in g/cm³): "))
volume = float(input("Enter volume (in cm³): "))

#find mass

if volume == 0 :
    print("Volume cannot be zero.")
else:
    mass = density*volume
    print(f"Mass is {mass} g.")