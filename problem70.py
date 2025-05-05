#chechk duplicationn odf studentid in student list
num = int(input("Enter a number : "))

std_lst = []

for i in range(num):
    std_lst.append(int(input("Enter std number : ")))

def duplication(st_lst):
    for i in st_lst:
        if st_lst.count(i)>1:
            return True
    return False

result = duplication(std_lst)

if result:
    print("Duplication")
else:
    print("Not a duplicate")