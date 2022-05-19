a=[]
b={}

n=int(input("Range:"))
for x in range(n):
    c=input('Name:')
    a.append(c)
print(a)
for y in a:
    if y in b:
         b[y]=b[y]+1
    else:
        b[y]=1
for z in b:
    print(z,':',b[z])
