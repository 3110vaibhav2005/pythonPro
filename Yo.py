print("This web site is for smaller student.")
a=input("Name:")
print("Hello ",a,"Welcome to learning counting.")
b=int(input("Age:"))
if(b<15):
    print("Get started learning.")
    i=int(input("Enter Number :"))
    if(i<101):
        while(i<100):
            i=i+1
            print(i)
            continue
            print("Thank You for learning.")
        else:
            print("Thank you for learning there is counting from 1to 100")
else:
    print("You are not a kid.")
