# get a username from the user that should have alphanumeric character then pass the username to function as parameter to display the username

# username = input("Enter username : ")


# def user(user_name):
#     if username.isalnum():
#         print("THE username is {}".format(username))
#     else:
#         print("The username contain special character or spaces so its not confirm.")
# user(username)

# check username alphanumeric character then pass the username to function as parameter to display the usernaem or check the length is not less than 8 or eqaul to 8

username  = input("Enter username : ")

def check_user(user_name):
    if username.isalnum():
        if len(username):
            print("The length of username is more than 8 and the username character contain alphanumeric the username is {}.".format(username))
        else:
            print("The length is not more than 8 or equal to 8, the username must contain alphanumeric character the username is {}.".format(username))
    else:
        print("The username not contain alphanumeric character not length is not more than the username is {}.".format(username))
check_user(username)