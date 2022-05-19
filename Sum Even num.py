print("To find sum all even no between the range given by you:")
a=0
b=int(input("The no from where you want to start:"))
c=int(input("The no from where you want to end:"))
for x in range(b,c+1):
    if x%2==0:
        a+=x
print("The sum of even no in range you dicide :",a)
