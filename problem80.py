# write a python program to print characters from string that are present at an odd index number 

sent = input("Enter a sentence : ")

if sent[0::-1]%2!=0:
    print("This characters is on odd indexing number =",sent)
else:
    print("This character is not on odd indexing number.")