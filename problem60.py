author_books = {}

for i in range(3):
    author_name = input("Enter authors name : ")
    book_name = input("Enter authors book name : ")
    author_books[author_name] = book_name
last_author = list(author_books.keys())[-1]

print("Last author name : ",last_author)
print("Their book name : ",author_books[last_author])