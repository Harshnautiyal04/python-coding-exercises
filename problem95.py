#Wite a python program mto get 10 data item from user how much integer float and string data type of data is stored in a list


# num = int(input("Enter number : "))

# lst = [34,'sneharsh','harsh','sneha',5.6,45.23,87.34,2931,53,623,9,3]
# int_type = 0
# float_type = 0 
# str_type = 0 

# for j in lst:
#     if(type(j) == int):
#         int_type += 1
#     if(type(j) == float):
#         float_type+= 1
#     if(type(j) == str):
#         str_type+= 1


# print("Integer data type =",int_type)
# print("Float data type =",float_type)
# print("String data type =",str_type)

# write a python program to get 10 float data type from user. system should convert float data type data to integer 
lst =[]

for i in range(4):
    lst.append(float(input("Enter number to store in a list : ")))

for i in lst:
    integer = int(i)
print(type(integer))