"""12. Write a python program to generate the following type of pattern for the given N rows
where N<=26
A
A B
A B C D
A B C D E (PUQ)"""

n= int(input("Enter the value of N : "))
asci=65
for i in range(1,n+1):
    asci=65
    for j in range(1,i+1):
        print(chr(asci),end=" ")
        asci=(asci+1)
    print()