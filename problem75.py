# write a python program to clone or copy of a 10 color list
# num = int(input("Enter number "))
# lst = []

# for i in range(num):
#     lst.append(input("Color name : "))
# print("Original list!")


# print(lst)

# lst_clone =lst.copy()

# print("Clone of a list!")

# print(lst_clone)
product = 1
summ = 0 
# write a program to get 10 number store into a list from the user  find thier products and sum then add both result and display to the user 

num  =int(input("Enter number : "))

lst = []

for i in range(num):
    lst.append(int(input("Number stored in a list : ")))

for i in lst:
    product *=i
    summ +=i
print(f"Product of number in a list is {product}.")
print(f"Sum of number in a list is {summ}.")

add = product+summ

print(f"Additon of product and sum of number present in a list is {add}.")



