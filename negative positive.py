a=[]
N=[]
p=[]
n=int(input("Range:"))
for x in range(n):
    d=int(input("All integer:"))
    a.append(d)
for y in a:
    if y>0:
        p.append(y)
    elif y<0:
        N.append(y)
print("all negative value:",N)
print("positive value",p)
