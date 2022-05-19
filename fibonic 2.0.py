a=0
b=1
n=int(input("Last term:"))
if n==1:
    print(a)
    print(b)
else:
    print(a)
    print(b)
    for x in range(2,n):
        c=a+b #c=0+1
        a=b   #a=1
        b=c   #b=a+b=c=1+1
        print(c)
