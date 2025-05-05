# write a python program to print first and last character from a string 

# sent = input("Enter a sentence : ")


# print("First character of a sentence is =",sent[0])

# print("Last character of sentence is =",sent[-1])
 

#write a python program to remove first and last character from a string 

sent = input("Enter a sentence : ")

if len(sent)<=2:
    result = ""
else:
    result = sent[1:-1]

print(f"String after removing first and last character = {result}")