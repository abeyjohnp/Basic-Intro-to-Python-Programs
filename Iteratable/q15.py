"armstrong number"
number=int(input("ENTER THE NUMBER : "))
sum=0
temp=number
while (number>0):
    sum+=(number%10)**3
    number=number//10
if (sum==temp):
    print("It is armstrong ")
else:
    print("It is not an armstrong number")


