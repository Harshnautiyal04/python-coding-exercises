#write a python program to display all students name except with start 'f' char

lst = []

for i in range(5):
    lst.append(input("Insert name to store in a list : "))

for i in lst:
    if not(i.lower().startswith('f')) and (i.endswith('n')):
        print(i)