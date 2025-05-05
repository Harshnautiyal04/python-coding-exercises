#create file get age and name and write on the file

# file = open("Harsh.txt","w+")
# name = input("Enter Your name : ")
# age = int(input("Enter your age : "))

# file.write(f"Your name is {name}.")
# file.write(f"Your age is {age}.")

# file.close()

# create a python program to read an existing file and get two number from the user and add them and displally the result in the existing file

file = open("Harsh.txt","a+")

file.seek(0)
print("File existing content.")
print(file.read())

num1 = int(input("Enter 1st number : "))
num2 = int(input("Enter 2nd number : "))

result = num1+num2 

file.write(f"The addition of {num1} and {num2} is {result}.")

file.close()
