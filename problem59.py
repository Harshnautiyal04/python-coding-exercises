
# get bio from the user and count no of words in the bio description

bio = input("Enter your bio : ")

l = len(bio)

print("Total char =",l)

bio_lst =len(bio.split())
print("Total words in bio",bio_lst)

# get bio from the user and count specific word in the bio
bio = input("Enter bio : ")
words = input("Enter word : ")

count = bio.lower().split().count(words.lower())

print(count)