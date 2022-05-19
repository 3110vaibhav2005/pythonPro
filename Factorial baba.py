n=int(input("Enter the num you want factorial of:"))
s=1             # in this s is taken as 1 because it can be value yu want but here it is correct as 1.
for v in range(0,n):
    v+=1        # in range 0 to n the loop check the conditon and return v+1 and assign to v.
    s*=v        # in this the assign value of v is checked and multiply in v and s. 
print("Factorials:",s)
# this prograam gives the factorial solution of given num
