'''
Write a Python program to read n integers 
into a list and separate the positive and negative numbers 
into two different lists. 
'''

n=int(input("Enter the number of elements : "))
l=[]
for i in range(n):
    i=int(input("Enter the number : "))
    l.append(i)

def positive(x):
    if (x>0):
        return True
    
def negative(x):
    if (x<0):
        return True
print("Positive : ", list(filter(positive,l)))
print("Negative : ", list(filter(negative,l)))

    
