a=int(input("Enter the lower limit : "))
b=int(input("Enter the upper limit : "))
sum=0
for i in range(a,b+1):
    if (i%2!=0):
        sum+=i
print("The sum is : ",sum)