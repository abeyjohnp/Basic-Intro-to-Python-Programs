"""Write a python program to count number of even numbers and odd numbers in a given set
of n numbers (PUQ)"""
even,odd=0,0
l=list(map(int,input("Enter a list : ").split())) #this is the statement used to input a list
for i in l:
    if i%2==0:
        even+=1
    else:
        odd+=1
print("Odd = ",odd,"\nEven = ",even)
