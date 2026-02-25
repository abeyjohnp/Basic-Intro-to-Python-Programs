x=int(input("Enter the value of x : "))
n=int(input("Enter the value of n : "))
sum=0
for i in range(n):
    prod=1
    j=1
    while(j<=i):
        prod=prod*j
        j+=1
    term=(x**i)/prod
    sum+=term
    
print("Sum is  : ", sum)