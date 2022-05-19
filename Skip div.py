n=int(input("The all No. you wnat to skip with divisibles:"))
n1=int(input("Starting Range:"))
n2=int(input("Ending Range:"))
for x in range(n1,n2+1):
    if x%n==0:
        continue
    print(x)
