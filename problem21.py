import array as arr

a = arr.array('i',[])

for i in range(5):
    a.append(int(input("Enter a number : ")))

m = a[0]
for j in range(5):
    print(a[j])
    if (a[j]<m):
        m = a[j]
print("Minimum number ",m)  