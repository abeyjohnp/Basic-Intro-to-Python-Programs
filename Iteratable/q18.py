startsal=float(input("Enter the starting salary : "))
percentinc=float(input("Enter the percentage of increase :"))
years=int(input("Enter the number of years: "))

print("\nYear     Salary")

currsal=startsal
for i in range(1,years+1):
    print(i,"\t",currsal)
    currsal+=currsal*(percentinc/100)