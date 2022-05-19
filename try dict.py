a={}
for x in range(3):
    name=input("name:")
    roll=int(input("roll no:"))
    mark=int(input("mark:"))
    print()
    a[name]=(roll,mark)
print(a)
for y in a:
    if a[y][1]>75:
        print(y,"\t",a[y][1])
