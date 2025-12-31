import math
#Approximating Square Roots
"""
set x to the users input value
set tolerance to 0.000001
set estimate to 1.0
while True
    set estimate to (estimate+x/estimate)/2
    set difference to abs(x-estimate**2)
    if difference <= tolerance:
        break
output the estimate
"""

x=int(input("Enter the value : "))
tolerance=0.000001
estimate=1.0
while True:
    estimate=(estimate+x/estimate)/2
    difference=abs(x-estimate**2)
    if difference<=tolerance:
        break
print("Estimated Square Root : ",estimate)

print("Python Build-in function Square Root : ",math.sqrt(x))