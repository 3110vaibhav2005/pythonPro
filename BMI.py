print("BMI Calculator")
weight=float(input("Enter Weight(Kg)\n:"))
height=float(input("Enter the Height(meters)\n:"))
BMI=weight/height**2
print("Your BMI is:",BMI)
if(BMI<=18.49):
    print("You are Underweight")
elif(BMI<=24.99 and BMI<=18.5):
    print("You are fit. Keep Maintaining your body.")
elif(BMI<=29.99 and BMI>=25.00):
    print("Over Weight.\nDo balanced Deit and Exercise.")
elif(BMI<=39.99 and BMI>=30.00):
    print("Obese.\nPlease do exerciseand less eating and talk to fitness coach.")
else:
    print("Morbidly Obsese")
