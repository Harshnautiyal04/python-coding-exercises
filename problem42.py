# # get input from user then square it and cube it and then do addition and multiply with result

# num = int(input("Enter number : "))

# print("Number\t\t Square\t\t Cube\t\t Addition")
# for i in range(1,num+1):
#     print("{}\t\t {}\t\t {}\t\t {}".format(i,i**2,i**3,i**2+i**3))


# get the number from the user but diffrence is 4 and then square and cube it and then do addition of cube and square

num = int(input("Enter number : "))

print("Number\t\t Square\t\t Cube\t\t Addition")

for i in range(1,num+1,3):
    print("{}\t\t {}\t\t {}\t\t {}".format(i,i**2,i**3,i**2+i**3))

