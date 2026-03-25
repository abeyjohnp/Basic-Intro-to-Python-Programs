nam=input("Enter the name of the member : ")
id=int(input("Enter the ID of the member : "))
age=int(input("Enter the age of the member : "))
membershiptype=input("Enter the type of membership : ")
allowedmembership=['basic','standard','premium']
monthlyfee=0
if membershiptype.lower() in allowedmembership:
    if membershiptype.lower() == 'basic':
        monthlyfee=700
    elif membershiptype.lower() == 'standard':
        monthlyfee=1200
    else:
        monthlyfee=1800
else:
    print("Input a valid membership")


days=int(input("Enter the number of days you have visited the gym : "))
totalvisits=[]
for i in range(days):
   mins=int(input("Enter the number of minutes visited during day "))
   totalvisits.append(mins)

print("Membership report \n")
print("Name : ",nam," ID : ",id," Age : ",age)
print("Total minutes spend : ",sum(totalvisits))
print("Average visit duration : ",sum(totalvisits)/len(totalvisits))
print("Longest visit : ",max(totalvisits))
print("Count of days with 0 minutes : ",totalvisits.count(0))

if (sum(totalvisits)/len(totalvisits))<20:
    monthlyfee+=100
    print("Penalty of ",100, " Rs added due to avg visit duration < 20 mins")

if (totalvisits.count(0))>20:
    monthlyfee+=200
    print("Penalty of ",200, " Rs added due to zero-attendance days > 20.")
if (days)>10:
    monthlyfee-=monthlyfee*0.05
    print("5% Discount applied!")

if (age)>60:
    monthlyfee-=monthlyfee*0.10
    print("10% Discount applied!")

print("Amount Payable : Rs ",monthlyfee)
