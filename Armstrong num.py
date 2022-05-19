n=int(input("Num: "))
n_copy=n
x=len(str(n))
asum=0
while n>0:
    num=n%10   
    asum+=num**x     
    n//=10
if n_copy==asum:
    print("The num:",n_copy,", is a Armstrong Num")
else:
    print("The given num:",n_copy,", is not a armstrong num.")
print("Thank You")
