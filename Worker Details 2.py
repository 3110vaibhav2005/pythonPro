worker={}
n=int(input("Range:"))
for x in range(n):
    na=input("Worker Name:")
    sal=int(input("Salary:"))
    print()
    worker[na]=sal
print("WorkerName----->Salary")
for y in worker:
    print(y,"------>",worker[y])
