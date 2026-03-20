import numpy as np
print("---MATRIX 1---")
r1=int(input("Enter the number of rows :"))
c1=int(input("Enter the number of coloumns : "))
a1=[]
for i in range(0,r1):
    temp=[]
    for j in range(0,c1):
        element=int(input())
        temp.append(element)
    a1.append(temp)
print("---MATRIX 2---")
r1=int(input("Enter the number of rows :"))
c1=int(input("Enter the number of coloumns : "))
a2=[]
for i in range(0,r1):
    temp=[]
    for j in range(0,c1):
        element=int(input())
        temp.append(element)
    a2.append(temp)
A=np.array(a1)
B=np.array(a2)
print(A,B)
print("RESULT AFTER ADDING : ",A+B)
print("RESULT AFTER SUBTRACTION : ",A-B)
print("RESULT AFTER MULTIPLICATION : ",np.matmul(A,B))
print("RESULT AFTER TRANSPOSE OPERATION (1): ",np.transpose(A))
print("RESULT AFTER TRANSPOSE OPERATION (2): ",np.transpose(B))



        