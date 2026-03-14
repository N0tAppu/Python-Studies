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
        quandity = float(input("Enter Quandity: "))
        while quandity <=0:
            print("Inavlid Quandity for Item!!. Try Again")
            quandity = int(input("Enter Quandity: "))
        cart[name] = price
        cart["Quandity"] = quandity
        cart["Total"] = price*quandity
        carts[name] = cart
        print("Item Added to Cart Successfully!")

    elif choice ==2:
        if len(carts) == 0:
            print("Your Cart is Empty!")
        else:
            print("Displaying All Items in Cart \n")
            for item in carts:
                for key,val in cart[item].items():
                    print(key,"\t",val)
    elif choice == 3:
        if len(carts) == 0:
            print("YOur Cart is Empyt!")
        else:
            print("\nTotal Price for All Items: ")
            totalc =0
            for item in carts:
                totalc += carts[item]["Total"]
            print(totalc)
    elif choice == 4:
        flag = False
        print("Exiting Program...")
    else:
        print("Invalid Choice!")
        
