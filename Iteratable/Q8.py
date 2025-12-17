"""Write a python program to print all numbers between 100 and 1000 whose sum of digits is
divisible by 9. (PUQ)"""

for i in range(100,1001):
    sumofdigits=0
    temp=i
    while(temp>0):
        sumofdigits+=(temp%10)
        temp=temp//10
    if (sumofdigits%9==0):
        print(i,end=" ")