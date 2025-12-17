"""Write a python program to print all prime factors of a given number. (PUQ)"""
n= int(input("Enter a number : "))
factors=[]
factor=2
while (n>=2):
    if (n%factor==0):
        factors.append(factor)
        n=n/factor
    else:
        factor+=1
print(factors)