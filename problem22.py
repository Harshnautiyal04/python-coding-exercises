# get char input from the user if char is a,e,i,o,u print vowel rather constonants

# chr = input("Enter your character : ")

# if (chr == 'a' or chr == 'e' or chr == 'i' or chr == 'o' or chr == 'u'):
    # print("It is vowel.")
# elif chr == 'e':
#     print("It is vowel.")
# elif chr == 'i':
#     print("It is vowel.")
# elif chr == 'o':
#     print("It is vowel.")
# elif chr == 'u':
#     print("It is vowel.")
# else:
#     print("It is consonant.")

# check it is alpha character whetehr vowel or consonant or if number is given by user says it is a number

char = input("Enter a character or number : ")


if (char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u'):
    print("It is vowel.")
elif char.isnumeric():
    print("It is a number.")
else:
    print("It is consonants.")