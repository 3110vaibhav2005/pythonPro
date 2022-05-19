n=int(input("Num:"))
n_copy=n
vsum=0
while n>0:
    num=n%10
    vsum=vsum*10+num
    n//=10
if n_copy==vsum:
    print("The given num:",n_copy,", is a Palindrome Num")
else:
    print("The given num is not a Palindrome num.")
