# write a python program to get a sentence from user the system should display only ten character maximum

# sent = input("Enter a sentence : ")

# if len(sent)<10:
#     print("The maximum length of the sentence is only 10.")
# else:
#     print(sent[slice(0,11)])
     

# write a python program to get a sentence from user the system should display all character except only last ten character maximum

sent = input("Enter a sentence : ")

if len(sent)<=10:
    print("The sentence is too short. Nothing to display.")
else:
    output = sent[:-10]
    print("Output (without last 10 characters):",output)
     
