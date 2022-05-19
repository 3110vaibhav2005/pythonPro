a=[]
b=[]
n=int(input("Range:"))
for x in range(n):
    c=input("Data:")
    a.append(c)
print(a)
print(b)

for y in a:
    if y not in b:
        b.append(y)
print(b)
