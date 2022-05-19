a=list(range(0,51,4))
b=[]
print(a)
for A in a:
    if not A%3:
        b.append(A)
print(b)
