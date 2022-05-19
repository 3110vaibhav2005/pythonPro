print("Geometric Progration Problems...")
a=float(input("First Term :"))
r=float(input("Comman Ratio :"))
n=float(input("No. of terms :"))
An=a*r**n-1
Sn=a*(1-r**n)/1-r
print("Last term :",An)
print("Sum of all terms:",Sn)
print("Thank You to use G.P Calculater")