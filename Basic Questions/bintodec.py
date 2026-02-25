n=input("Enter the number : ")
decimal=0
length=len(n)-1
for i in n:
    decimal+=int(i)**length
    length-=1
print("The decimal number = ",decimal)