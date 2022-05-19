a=[]
n=int(input("Range:"))
for x in range(n):
    c=int(input("Integer data:"))
    a.append(c)
print(a)
b={}
for x in a:
    if x not in b:
        b[x]=1
    else:
        b[x]=b[x]+1
print(b)
