a={}
while True:
    b=input("Key:")
    c=input("Value:")
    d=input("Want to exit enter 'n/N' else any key:")
    a[b]=c
    if d=='N' or d=='n':
        break
    else:
        print()
print("Dict:",a)

print('\nUse of len()')
print('len of dict:',len(a))
print('\nUse of get()')
e=input("Enter key wann serch:")
print('Value:',a.get(e,'not found!!!'))
