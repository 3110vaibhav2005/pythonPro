n=int(input("Range:"))
a=[]
for x in range(n):
    i=input("Input:")
    a.append(i)
print("List Is:",a)
s=input("")
if s in a:
    print("Element Found...")
    print("Index of element:",a.index(s))
else:
    print("Element Not found...")
