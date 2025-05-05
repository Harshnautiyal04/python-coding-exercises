# get six identity number from the user and show them in descending order

# num = int(input("Enter a number  : "))

# lst =[]

# for i in range(1,num+1):
#     lst.append(int(input("Enter number to store in a list : ")))
# lst.sort(reverse = True)
# print("Numbers in descending order =",lst)

# get six idendity from the user and show them in list and after clear the list and show empty list


num = int(input("Enter a number : "))

std_lst = []

for i in range(num):
    std_lst.append(int(input("Enter a number : ")))
std_lst.clear()
print(std_lst)
