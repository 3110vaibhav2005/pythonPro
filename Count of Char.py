Dict={}
a=input("Enter String:")
for x in a :
    if x not in Dict :
        Dict[x]=1
    else:
        Dict[x]=Dict[x]+1
print("Count of Charecter....")
print(Dict)
