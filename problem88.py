#write a python program to genrate number from 0 to 20 only even number and generate 0 to 20 odd number. add both generated number to each other to display total result

# s1 = 0
# s2=0
# for i in range(2,21,2):
#     s1+=i
# print("Sum of even number from 1 to 20 is",s1)

# for j in range(1,21,2):
#     s2+=j
# print("Sum of odd number from 1 to 20 is",s2)

# add = s1+s2

# print("The result is",add)

#write a python program to genrate number from 0 to 20 only divisible by 3 and generate 0 to 20 only divisible by 5. add both generated number to each other to display total result

s1 = 0
s2=0
for i in range(1,21):
    if i%3==0:
        s1+=i
print("Sum of 1 to 20 number that is divisible by 3 is",s1)

for j in range(1,21):
   if j%5==0:
       s2+=j
print("Sum of 1 to 20 divisible by 5 is",s2)

add = s1+s2

print("The result is",add)