# write a prgram to make average calculator 
# num = int(input("Enter a number : "))
# lst =[]
# total = 0
# for i in range(num):
#     lst.append(int(input("Enter numbers : ")))

# for j in lst : 
#     total+=j

# avg = total/num

# print(avg)

# write a program to make a calculator to binary to decimal number 

binary = input("Enter a binary number : ")

if not all(bit in '01' for bit in binary):
    print("Invalid Binary number. Please enter only 0s and 1s.")
else:
    decimal = int(binary,2)
print(f"The decimal value of binary {binary} is {decimal}.")