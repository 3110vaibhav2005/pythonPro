n=eval(input('List only:'))
def bs(l):
    n=len(l)
    for x in range(n-1):
        for y in range(0,n-x-1):
            if l[y] <l[y+1]:
                l[y+1],l[y]=l[y],l[y+1]
bs(n)
print(n)