# get 5 number in the list pass that list in the function to multiply and add that number and display total result

# lst = []

# for i in range(1,6):
#     lst.append(int(input("Enter number : ")))

# def add_mul(lst_num):
#     s=0
#     m=1
#     for i in lst_num:
#         s+=i
#         m*=i
#     print("Addition =",s)
#     print("Multiplication =",m)
# add_mul(lst)
    
# get 5 number in the tuple pass that list in the function to multiply and add that number and display total result


tup = ()

temp_tup =[]
for i in range(1,6):
    temp_tup.append(int(input("Enter number : ")))
tup = tuple(temp_tup)
print(tup)

def add_mul(tup_num):
    s=0
    m=1
    for i in tup_num:
        s+=i
        m*=i
    print("Addition =",s)
    print("Multiplication =",m)
add_mul(tup)
