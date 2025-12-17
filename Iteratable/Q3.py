#The factorial of an integer N is the product of the integers between 1 and N, inclusive.
#Write a while loop that computes the factorial of a given integer N.

n=int(input("Enter the number : "))
product=1
i=1
while (i<=n):
    product*=i
    i+=1
print("Factorial of ",n," is ",product)