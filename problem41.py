# write a python program to get a angle from the user and its sin and cos value in radian


# import math

# angle = float(input("Enter angle value : "))

# sin_value= math.sin(angle)

# cos_value = math.cos(angle)

# print("The value of sin {} in radian is ".format(angle),sin_value)

# print("The value of cos {} in radian is ".format(angle),cos_value)

# write a python program to get a angle from the user and its sin and cos value in degree


import math

angle = float(input("Enter angle value : "))

sin_value= math.sin(angle)

cos_value = math.cos(angle)

print("The value of sin {} in radian is ".format(angle),sin_value)

print("The value of cos {} in radian is ".format(angle),cos_value)


sin_result = math.degrees(sin_value)
cos_result = math.degrees(cos_value)


