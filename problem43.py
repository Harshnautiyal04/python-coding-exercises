# write a program to get starting  number and ending number from the user and display that number with proper sequence 

num = int(input("Enter a number : "))

if num>=5 and num<6:
    for i in range(num,11):
        print(i)
else:
    print("Number is less than 5")
        