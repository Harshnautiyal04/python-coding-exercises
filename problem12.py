# Write a python program to display star pattern
# for i in range(1,6):
#     for j in range(i):
#         print("*",end=" ")
#     print(" ")

for i in range(5,0,-1):
    for j in range(1,i+1):
        print(" ",end =" ")
    for k in range(5,i-1,-1):
        print("*",end = " ")
    print()
