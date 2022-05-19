from random import *
from winsound import *
print('*'*75)
print("Luck Game...")
print('*'*75)

while True:
    a=int(input("Enter any num 0-9:"))
    b=randint(0,9)
    if a==b:
        print("Congratulations...\nThank you for try...")
        Beep(1500,250)
        Beep(1500,250)
        Beep(1500,250)
        Beep(1500,250)
        Beep(1500,250)
        Beep(1500,250)
        Beep(1500,250)
        
        break
    else:
        print("Try again...")
