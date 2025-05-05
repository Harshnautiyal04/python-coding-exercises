# write a python program  to get memory into gb and convert gb into bytes


# GB = int(input("Enter memory size : "))

# print(f"The {GB} in memory.")

# bytes_value = GB*1024*1024*1024

# print(f"The {GB} gb value in bytes is {bytes_value}.")


# write a python program to get memory in bytes and convert bytes into gb

byte = int(input("Enter bytes value : "))

print(f"The value of {byte} bytes in memory.")

gb = byte/(1024**3)

print(f"The value of {byte} byte is converted into {gb} gb.")