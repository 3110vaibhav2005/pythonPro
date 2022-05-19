print('''Hello Survivors welcome to our E-Sports Registration Portal>
Here you can register for India's BattelGround E-Sport Tournament.
The Games you can Register are:
1. Garena Free Fire
2. Battel Ground Mobile India(BGMI)
3. Call Of Duty(COD)
4. Minecraft(Bed War)
The Tournament are in SOLO/DUO/SQUAD.
The Tournament date is 2/Feb/2022 & last date for registration is 10/DEC/2021.
To participate in Tournament please fill the following details.''')
NAME=input("Please Enter Name:")
print("Welcom",NAME)
AGE=int(input("Age:"))
if(AGE>=18):
    UID=int(input("Please enter In_Game UID:"))
    name=input("In_Game Name:")
    Mode=input("Mode you want to play SOLO/DOU/SQUAD:")
    DOB=input("DATE OF BIRTH in dd/mm/yyyy:")
    Contact=int(input("Phone No."))
    MAIL=input("Email Id :")
    mode=["Duo","Squad"]
    if(Mode is mode):
        print("If your mode is Duo, in player2&3 UID enter (00).")
        CP=input("Captain IN_GAME name:")
        CP1=int(input("Captain IN_GAME UID:"))
        P2=input("Player 1 IN_GAME name:")
        P2a=int(input("Player 1 IN_GAME UID:"))
        P3=input("Player 2 IN_GAME name:")
        P3a=int(input("player 2 IN_GAME UID:"))
        P4=input("Player 3 IN_GAME name:")
        P4a=int(input("Player 3 IN_GAME UID:"))
    else:
        print("Thank You")
else:
    print("Try next time ")
