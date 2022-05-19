a=input('Phara:')
l=0
u=0
d=0
ai=0
for i in range(a):
    if i.islower():
        l+=1
    if i.isupper():
        u+=1
    if i.isdigit():
        d+=1
    if ai.isalpha():
        ai+=1
print('The lower case in given phara:',l)
print('The upper case in given phara:',u)
print('The digit in given phara:',d)
print('The alphabet in given phara:',ai)
