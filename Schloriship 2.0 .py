print("Hello User...\nSchlorship form")
a=input("Name:\n")
b=int(input("Age:\n"))
bb=int(input("Enter the current class:"))
if(15>=b<=17 and bb<=10):
    c=int(input("Phone no.:\n"))
    d=input("Date of birth \t(dd/mm/yyyy):\n")
    e=input("Father Name:\n")
    f=input("Enter Mother Name:\n")
    i=input("Enter the Address:\n")
    g=int(input("Class You passed now:\n"))
    h=int(input("Percentage Of your Child in 10:\n"))
    i=int(input("The current class in which your child is :\n "))
elif(b<=18 and bb==12):
    c1=int(input("Phone no.:\n"))
    d1=input("Date of birth \t(dd/mm/yyyy):\n")
    e1=input("Father Name:\n")
    f1=input("Enter Mother Name:\n")
    i1=input("Enter the Address:\n")
    f1=int(input("Enter Addhar No.:\n"))
    h2=int(input("Percentage in class 10 :\n"))
    i2=int(input("Enter the class 12 percentage:\n"))
    g2=input("The current Course in you are")
else:
    print("You does't meet our requirenment..\n Sorry",a)
