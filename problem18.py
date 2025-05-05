#store the name ,address,contact info in dictionry and dispaly them after this update contact no and again display updated dictionary


# print("First Record.")
# d = {"Name":"Harsh","Address":"Delhi","CNO":87943823}
# print(d)

# print("Updated Record.")
# d.update({"CNO":46356782})
# print(d)

#store thr name,address,contaxxt no and then update it but runtime sstore in dictinary

user_info = {"name":"lala","address":"matiyala","CNO":37858943}

print(user_info)

CNO = int(input("Enter Your contact number : "))
user_info.update({"CNO":CNO})
print(user_info)