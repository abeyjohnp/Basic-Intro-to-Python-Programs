from math import sqrt
x1=int(input("Enter x1 point : "))
y1=int(input("Enter y1 point : "))
x2=int(input("Enter x2 point : "))
y2=int(input("Enter y2 point : "))
#root of (x2-x1)^2 + (y2-y1)^2
print(((x2-x1)**2 + (y2-y1)**2)**0.5) 

#or you can print using math function
print(sqrt((x2-x1)**2 + (y2-y1)**2))
