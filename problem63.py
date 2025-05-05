# write a program find a max number from a list 

num = int(input("Enter a number : "))

lst = []

for i in range(num):
    lst.append(int(input("Enter a number : ")))
    # m=max(lst)

def max_value(m):
    return max(m)
print(f"The maximum value among the {lst} is {max_value(lst)}.")