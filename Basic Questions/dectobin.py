n=int(input("Enter a decimal number to convert to binary number : "))
bin=""
while (n>0):
    remainder=n%2
    n=n//10
    bin=str(remainder)+bin

print("The binary notation for the decimal number is : "+bin)

