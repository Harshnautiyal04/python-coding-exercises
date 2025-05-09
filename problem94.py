#write a python program to get number from user to display table reverse order 
# example :
# 2*10 = 20 
# 2*9 = 18 and so on 

# num1 = int(input("Enter a number : "))

# num2 = int(input("Enter a number : "))

# for i in range(num1,0,-1):
#     print(f"The table of 2 is {i}*{num2} = {i*num2}")


# write python program to get number from usr to display table in reverse order. Number should multiply with odd numbers only 

num1 = int(input("Enter number : "))

num2 = int(input("Enter number : "))

for i in range(num1,0,-1):
     if i%2 !=0:      
        print(f"The table of {num2} is {i}*{num2} = {i*num2}")