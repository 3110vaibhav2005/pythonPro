worker=dict()
n=int(input("Number of worker:"))
for x in range(n):
    name=input("Enter the name of worker:")
    salary=int(input("Salary (Rs):"))
    worker[name]=salary
print("\nWorkerName\t\tSalary")
for y in worker:
    print(y,"\t\t\t",worker[y])
