# write a python program to search any character or a set of character from a string 

# sent = input("Enter a sentence : ").lower()

# word = input("Enter a set or character : ").lower()

# if word in sent:
#     print("Yes! This character present in a sentence.")
# else:
#     print("No! This character is not present in a sentence.")


# write a python program to get a sentence from a user, user should able to remove any character from a string 

sent = input("Enter a sentence : ")

ch = input("Enter the character you want to remove : ")

if len(ch) !=1:
    print("Please enter exactly one character to remove.")
else:
    updated_sentence = sent.replace(ch,"")

print("Updated sentence :",updated_sentence)
