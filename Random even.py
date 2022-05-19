from random import *
print('*'*75)
print('Any Even random num between 0-100')
print('*'*75)
while True:
    print(randrange(0,101,2))
    a=input('if stop enter (n/N):')
    if a=='n' or a=='N':
        break
