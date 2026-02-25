s1= float(input("Enter the first side : "))
s2= float(input("Enter the second side : "))
s3= float(input("Enter the third side : "))

if (s1**2==s2**2+s3**2) or (s2**2==s1**2+s3**2) or (s3**2==s1**2+s2**2):
    print("It is a right triangle")
else:
    print("It is not a right triangle")