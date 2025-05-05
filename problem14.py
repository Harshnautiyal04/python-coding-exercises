# write  a program to get 6 numbers in the list and sum that numbers.
# s = 0
# lst = []
# for i in range(6):
#     lst.append(int(input("Enter number : ")))  
# # print(lst)

# for i in lst:
#     s+=i
# print("Sum the number present in the list is ",s)

# write a program and get 6 number in the tuple and sum that numbers

tup = ()
temp_tup = list(tup)
for i in range(6):
    temp_tup.append(int(input("Enter a number : ")))
tup = tuple(temp_tup)
print(tup)

s = 0
for i in tup:
    s+=i
print("Sum of tuple elements is ",s)