# write a python program to print characters from string that are present at an odd index number 

# sent = input("Enter a sentence: ")
# s = len(sent)

# for i in range(1, s + 1):
#     if i % 2 != 0:
#         print(sent[i - 1])

# write a python program to print characters from string that are present at an even index number 

sent = input("Enter a sentence: ")
s = len(sent)

for i in range(1, s + 1):
    if i % 2 == 0:
        print(sent[i - 1])

