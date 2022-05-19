a=[]
b=[]
n=int(input("Range:"))
for x in range(n):
    data=input("Data:")
    a.append(data)
print(a)
for y in a:
    if y not in b:
        b.append(y)
print(b)
