print("Welcome to Travel & Tour registration.")
a=input("Enter your name:")
d=int(input("No of people in trip :"))
if(d<=5):
    b=int(input("Enter Age:"))
    c=int(input("Phone No. :"))
    e=("Mumbai","Srinagar","Manali","Visakhapatnam","Agar","Jaipur","and your choice")
    print("The visiting places are:\n",e)
    e1=("Enter the place you want to go:")
    if(e1==e[0]):
        print("The price of Mumbai is Rs 2000 perperson.")
    elif(e1==e[1]):
        print("The price of Srinager is Rs 5000 perperson.")
    elif(e1==e[3]):
        print("The price of Manali is Rs 5000 perperson.")
    elif(e1==e[4]):
        print("The price of Visakhapatnam is Rs 3000 perperson.")
    elif(e1==e[5]):
        print("The price of Agar is Rs 2500 perperson.")
    elif(e1==e[6]):
        print("The price of Jaipur is Rs 3000 perperson.")
    else:
        print("We will send the details on Mails")
    if(d==1):
        g=input("Enter The person Name:")
        print("The details were sent on Mail\nThank for Registration ")
    elif(d==2):
        g=input("Enter The person 1 Name:")
        g1=input("Enter The person 2 Name:")
        print("The details were sent on Mail\nThank for Registration ")
    elif(d==3):
        g=input("Enter The person 1 Name:")
        g1=input("Enter The person 2 Name:")
        g2=input("Enter The person 3 Name:")
        print("The details were sent on Mail\nThank for Registration ")
    elif(d==4):
        g=input("Enter The person 1 Name:")
        g1=input("Enter The person 2 Name:")
        g2=input("Enter The person 3 Name:")
        g3=input("Enter The person 4 Name:")
        print("The details were sent on Mail\nThank for Registration ")
    elif(d==5):
        g=input("Enter The person 1 Name:")
        g1=input("Enter The person 2 Name:")
        g2=input("Enter The person 3 Name:")
        g3=input("Enter The person 4 Name:")
        g4=input("Enter The person 5 Name:")
        print("The details were sent on Mail\nThank for Registration ")
    else:
        print("sorry")
else:
    print("We are very sorry we can not afford",d,"people trip. \n Thank you.")
        
