a=[4,29,2,-7,100]
b=a
a=a.sort
print(a)
for x in range(len(a)):
    if b[x]==a[0]:
        print(a)
        print(b)
        print(a[0],"is smallest element at index",x)
