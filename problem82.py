# write a python program to append those number that are divisible by 5 and 7 .range take input from the user new created list
# num = int(input("Enter number : "))
# lst = []
# new_lst = []
# for i in range():
#     lst.append(int(input("Enter number to store in a list : ")))

# for i in lst:
#     if i % 5 == 0 and i % 7 == 0:
#         new_lst.append(i)

# print(f"Number that are divisible by 5 and 7 are {new_lst}.")
        

# write  python program to check wheather username is encrypted form or not



num = int(input("How much username you want enter number : "))

username = input("Enter a username : ").lower()

lst = []

for i in range(num):
    lst.append(input("Enter username you want to store in a list : ").lower())

if any(word in username for word in lst):
    print("This looks like a normal username.")
elif len(username) > 12 and not username.isalnum():
    print("This looks like an encrypted username.")
else:
    print("This looks like a normal username.")