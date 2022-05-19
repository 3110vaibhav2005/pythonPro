a=input("Enter String:")
b={}
for x in a:
    if x not in b:
        b[x]=1
    else:
        b[x]=b[x]+1
print(b)
