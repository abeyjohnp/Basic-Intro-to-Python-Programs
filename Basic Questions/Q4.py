hourlywage=int(input("Enter the hourly wage : "))
totalregularhours=int(input("Enter the total regular hours : "))
totalovertimehours=int(input("Enter the total overtime hours :"))
overtimepay=totalovertimehours*1.5*hourlywage
totalweeklypay=hourlywage*totalregularhours+overtimepay
print("Total weeklypay= ", totalweeklypay)