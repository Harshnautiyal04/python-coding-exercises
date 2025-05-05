# write a python program  to get 5 color name from the user in list and display the list,remove last color  and display all the colors for the user

# color = []

# num = int(input("Enter a number : "))
# for i in range(num):
#     color.append(input("Enter color : "))

# print("New list.")
# print(color)

# color.pop()

# print("Updated list.")

# print(color)

#  get 5 color from the user in list and display the list remove fist colr from the list and display the list

color = []

num = int(input("Enter the number : "))

for i in range(num):
    color.append(input("Enter the color : "))

print("Current list.")
print(color)

color.pop(0)
print("Updated list.")

print(color)