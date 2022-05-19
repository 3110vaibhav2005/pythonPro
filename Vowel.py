a=input("Word:")
v=['a','e','i','o','u','A','E','I','O','U']
num=0
for x in a:
    if x  in v:
        num=num+1
print("The num of time  Vowels in given word is:",num)
