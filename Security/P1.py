'''ENCRYPTION'''
a=input("Enter the text : ")
distance=5
chiperstring=""
for i in a:
    ci=(ord(i)+distance)
    if ci>ord('z'):
        ci=ci-26
    chiperstring+=chr(ci)
print("Cipher string is : "+ chiperstring)

'''DECRYPTION'''

newstring=""
for i in chiperstring:
    ci=(ord(i)-distance)
    if ci<ord('a'):
        ci+=26
    newstring+=chr(ci)

print("The original string is  : "+newstring)