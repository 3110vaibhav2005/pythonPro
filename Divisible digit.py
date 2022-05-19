digit=int(input("Any no:"))
for x in range(1,100):
    if x%digit==0:
        digit+=x
print("The sum digit divisible by the digit given by user is:",digit)
