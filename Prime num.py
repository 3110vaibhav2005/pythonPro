n=int(input("Num:"))
for x in range(2,n):
    if n%x==0:
        print("The given num is not a prime.")
        break
else:
    print("The given num is prime.")

