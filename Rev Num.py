n=int(input("Any num tro reverse:"))
num=0
while n!=0:
    num_n=n%10
    num=num*10+num_n
    n//=10
print("Rev. num:",num)
