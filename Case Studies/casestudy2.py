menu = {
    "Starters": {"Soup": 120, "Spring Roll": 150},
    "Main Course": {"Fried Rice": 250, "Paneer Curry": 300},
    "Desserts": {"Ice Cream": 100, "Gulab Jamun": 80},
    "Beverages": {"Tea": 40, "Coffee": 60}
}
def display_menu():
    print("-"*20)
    print("\tMenu")
    print("-"*20)
    for i in menu:
        print(i)
        for j in menu[i]:
            print("%15s"%j,end="")
            print(" : Rs %-4d" % menu[i][j])
display_menu()
order_list=[]
def take_order(order_list):
    item_name=input("Enter the name of the item : ")
    item_quantity=int(input("Enter the quantity : "))
    if (item_quantity<0):
        print("Enter a valid quantity!")
    else:
        flag=0
        for i in menu:
            for j in menu[i]:
                if item_name==j:
                    price=menu[i][j]
                    flag=1
        if (flag==1):
            order_menu={
                "item":item_name,
                "price":price,
                "quantity":item_quantity
            }
            order_list.append(order_menu)
        else:
            print("Invalid item!")
    if (input("Enter done if over, else just press any character : ").lower() != "done"):
        take_order(order_list)
    """
    else:
        print("-"*20)
        print("\tORDERED ITEMS")
        print("-"*20)
        print(order_list)"""

take_order(order_list)

def calculate_subtotal(order_list):
    subtotal=0
    for i in order_list:
        subtotal+=i['price']*i['quantity']
    return subtotal

def calculate_tax(subtotal):
    return subtotal*0.05

def calculate_discount(subtotal):
    if (subtotal>1000):
        return subtotal*0.1
    else:
        return 0

def generate_bill(order_list):
    subtotal = calculate_subtotal(order_list)
    tax = calculate_tax(subtotal)
    discount = calculate_discount(subtotal)
    final_amount = (subtotal + tax) - discount

    print("\n" + "-"*34)
    print("         RESTAURANT BILL")
    print("-"*34)
   
    print("%-15s %5s %7s %7s" % ("Item", "Qty", "Price", "Total"))

    for i in order_list:
        item_total = i['price'] * i['quantity']
        print("%-15s %5d %7d %7d" % (i['item'], i['quantity'], i['price'], item_total))
   
    print("-" * 34)
    print("%-25s %7.2f" % ("Subtotal:", subtotal))
    print("%-25s %7.2f" % ("GST (5%):", tax))
    print("%-25s %7.2f" % ("Discount:", discount))
    print("-" * 34)
    print("%-25s %7.2f" % ("Final Amount:", final_amount))
    print("-" * 34)

generate_bill(order_list)