# Get age and name from the user to ask him to participate or not in voting

# Age = int(input("Enter Your age : "))
# Name  = input("Enter your name : ")
# if Age>=18:
#     print("Hi {}! You are {} so you can participate in voting.".format(Name,Age))
# else:
#     print("Sorry,"+Name+"  You can not take participate this year you can participate after",18-Age,"Year!")

# Get marks from the user and his name and check he can take admiision in college or not.

Marks = float(input("Enter your marks : "))
Name = input("Enter Your name : ")

if Marks>=60:
    print("{} , You can take admission in this college!")
else:
    print("Sorry "+Name+"! You cannnot take the admission ,You need "+str(60-Marks)+" numbers more to take admission.")