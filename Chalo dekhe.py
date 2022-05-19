def Func1(A,B):
    if A % B == 0:
        return 10
    else:
        return A + Func1(A,B-1)
val = Func1(20,-21)
print(val)
