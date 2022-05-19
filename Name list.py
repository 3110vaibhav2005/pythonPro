A=[]
n=int(input("Range:"))
for x in range(n):
    a=input("Name:")
    A.append(a)
print(A)
s=input("Eneter name:")
if s in A:
    print("Location of ",s,"is:",A.index(s)+1)
