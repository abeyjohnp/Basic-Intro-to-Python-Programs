import math
a=float(input("Enter a : "))
b=float(input("Enter b : "))
c=float(input("Enter c : "))
d=b**2-4*a*c

if (d>0):
    #real & distinct roots
    print("The two real and distinct roots are : \n")
    print("Root 1 : ",(-b+math.sqrt(d))/2*a)
    print("Root 2 : ",(-b-math.sqrt(d))/2*a)

elif (d==0):
    print("Repeated Root : ",(-b)/2*a)

else:
    realpart=-b/2*a
    imgpart=math.sqrt(d)/2*a
    print("The complex roots are : ",realpart+imgpart,"i and",realpart-imgpart,"i")
    
