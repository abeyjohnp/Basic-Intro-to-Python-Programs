"""Write a python program to generate prime numbers within a certain range. (PUQ)"""
n1=int(input("Enter the first range : "))
n2=int(input("Enter the second range : "))
for i in range(n1,n2+1):
    flag=0
    for j in range(1,i+1):
        if (i%j==0):
            flag+=1
    if (flag==2):
        print(i," ")