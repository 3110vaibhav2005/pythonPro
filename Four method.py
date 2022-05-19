A=[]
n=int(input("Num of Student:"))
for x in range(n):
    st=input("Student:")
    A.append(st)

print('''
1. To insert the new data
2. To delete the data
3. To show the data
4. To update the data
''')

a=int(input('Enter the Choice:'))

if a==1:
    B=input("Enter the name:")
    A.append(B)
    print("The New data is:",A)
elif a==2:
    B=input("Enter the name you want to delete:")
    if B in A:
        A.remove(B)
        print(A)
    else:
        print("Name not found !")
elif a==3:
    print("All Students name are:",A)
elif a==4:
    B=input("Enter the student name:")
    A[A.index(B)]=input("New Student:")
    print(A)
