# write a python program  to count a specific word or character in a sentence
sent = input("Enter a sentence from user : ")
w_c=input("Enter a word or char to count : ")
count_sent=sent.count(w_c)

print(f"Your sentence {sent}.")
print(f"Number of words in a {sent} is {count_sent}.")
print(f"{count_sent} time {w_c} present in a sentence.")
