# write a python program to get password from the user and make sure that password should contain numbers and alphabetic

# password = input("Enter a strong password : ")

# if (password.isalnum()):
#     print("Your password {} is correct.".format(password))
# else:
#     print("Try again! Only alpha and numeric. No space or special character.")

# get password from the user password contain alphanumric and must the length is not greater than nor equal to 8.

pwd = input("Enter a strong password : ")


if (pwd.isalnum()):
    if len(pwd)<8:
        print("The password {} is alpha ,numeric and its length is not greater than 8.".format(pwd))
    else:
        print("The password is alphanumeric but the length is greater than or equal to 8.")
else:
    print("Try again! your password contain space ,special character and greater than 8 digit.")

    
