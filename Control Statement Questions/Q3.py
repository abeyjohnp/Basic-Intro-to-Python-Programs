#using match case

month=input("Enter the month number : ")
match month:
    case "1":
        print("31")
    case "2":
        print("28")
    case "3":
        print("31")
    case "4":
        print("30")
    case "5":
        print("31")
    case "6":
        print("30")
    case "7":
        print("31")
    
    case "8":
        print("31")
    case "9":
        print("30")
    case "10":
        print("31")
    case "11":
        print("30")
    case "12":
        print("31")


#using elif ladder
month=int(input("Enter the month number : "))
if month==1:
    print(31)
elif month==2:
    print(28)
elif month==3:
    print(31)
elif month==4:
    print(30)
elif month==5:
    print(31)
elif month==6:
    print(30)
elif month==7:
    print(31)
elif month==8:
    print(31)
elif month==9:
    print(30)
elif month==10:
    print(31)
elif month==11:
    print(30)
elif month==12:
    print(31)
