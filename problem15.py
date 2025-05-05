# write a program to get 6 numbers in the list and display all number then clear list and then display

# lst = []

# for i in range(6):
#     lst.append(int(input("Enter a number : ")))
# print(lst)

# lst.clear()
# print(lst)


# write a program to get 6 numbers in the list and display all number then clear list and display

tup = ()
temp_tup = list(tup)

for i in range(6):
    temp_tup.append(int(input("Enter numbers : ")))
tup = tuple(temp_tup)
print(tup)

temp_tup.clear()

tup = tuple(temp_tup)
print(tup)


