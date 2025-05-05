# write a python program get number from user in array and sum all number and display
# import array as arr

# a = arr.array('i',[])
# s=0

# for i in range(5):
#     a.append(int(input("Enter numbers to store in an array = ")))
# for j in range(5):
#     print(a[i])
#     s+=a[i]

# print("Sum of array elements is ",s)



import array as arr

a = arr.array('i',[])

for i in range(5):
    a.append(int(input("Enter an array number : ")))
    print(a[i])
    mx =max(a)
print("The maximum value an array is ",mx)