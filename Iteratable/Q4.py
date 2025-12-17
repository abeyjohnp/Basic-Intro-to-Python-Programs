#Write a program to reverse a given number and also find the sum of digits of the number.

number=int(input("Enter a number : "))
temp=number
rev=0
while(temp>0):
    rev=(rev*10)+(temp%10)
    temp=temp//10
print("Reverse of ",number," is ",rev)
