carts = {}
flag = True
while flag:
    print("""
========= SHOPPING CART ===========
          
1       Add Item
2       Display All items
3       Total Cost1
4       Exit Program
""")
    cart = {}
    choice = int(input("Enter your Choice: "))
    if choice ==1:
        name = str(input("Enter Item name: "))
        price = float(input("Enter item price: "))
        quantity = float(input("Enter Quantity: "))
        while quantity <=0:
            print("Inavlid Quantity for Item!!. Try Again")
            Quantity = int(input("Enter Quantity: "))
        cart["Price"] = price
        cart["Quantity"] = quantity
        cart["Total"] = price*quantity
        carts[name] = cart
        print("Item Added to Cart Successfully!")

    elif choice ==2:
        if len(carts) == 0:
            print("Your Cart is Empty!")
        else:
            print("Displaying All Items in Cart \n")
            for item in carts:
                print("\nItems: ",item)
                for key,val in carts[item].items():
                    print(f"{key:<12} : {val}")
                print()
    elif choice == 3:
        if len(carts) == 0:
            print("Your Cart is Empyt!")
        else:
            totalc =0
            print("\nTotal Price for All Items in Cart: ",end = "")
            for item in carts:
                totalc += carts[item]["Total"]
            print(totalc)
    elif choice == 4:
        flag = False
        print("Exiting Program...")
    else:
        print("Invalid Choice!")
        
