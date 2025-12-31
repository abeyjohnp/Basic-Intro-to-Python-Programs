"""Write a python program to find the sum of cosine series 1-x 2 /2!+x 4 /4!-…. (PUQ)"""

#we use the formula cos x = 1 - (x2 / 2 !) + (x4 / 4 !) - (x6 / 6 !) +...

import math
n = int(input("Enter the number of terms: "))
x = int(input("Enter the angle : "))
x= math.radians(x)
sum = 1.0
i=1
while (i<=n):
    fact=1
    j=1
    while (j<=n):
        fact*=j
        j+=1
    if (i%2==0):
        sum+=pow(x,2)/fact
    else:
        sum-=pow(x,2)/fact
    i+=1
print(sum)
    