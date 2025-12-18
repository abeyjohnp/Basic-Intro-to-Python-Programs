x=int(input("Enter the base number : "))
y=int(input("Enter the exponent : "))
res=x
#2*4 = 2*2*2*2
#6*2 = 6*6
i=1
while (i<y):
    res=res*x
    i+=1
print("The result is : ",res)