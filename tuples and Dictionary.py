carts = {}
flag = True
while flag:
    print("""
========= SHOPPING CART ===========
          
1       Add Item
2       Display All items
3       Total Cost
4       Delete Item
5       Exit Program
""")
    cart = {}
    choice = int(input("Enter your Choice: "))
    if choice ==1:
        name = str(input("Enter Item name: "))
        uid = int(input("Enter Item Uid: "))
        price = float(input("Enter item price: "))
        quantity = float(input("Enter Quantity: "))
       
        while quantity <=0:
            print("Invalid Quantity for Item!!. Try Again")
            quantity = int(input("Enter Quantity: "))
            
        if uid in carts:
            print("Error, UID already in use")
        else:
            cart["Name"] = name
            cart["Price"] = price
            cart["Quantity"] = quantity
            cart["Total"] = price * quantity

            carts[uid] = cart
            print("Item Added Successfully!")
        
    elif choice ==2:
        if len(carts) == 0:
            print("Your Cart is Empty!")
        else:
            print("Displaying All Items in Cart \n")
            for uid in carts:
                print("\nUID:", uid)
                for key,val in carts[uid].items():
                    print(f"{key:<12} : {val}")
                print()

    elif choice == 3:
        if len(carts) == 0:
            print("Your Cart is Empty!!")
        else:
            totalc =0
            print("\nTotal Price for All Items in Cart: ",end = "")
            for uid in carts:
                totalc += carts[uid]["Total"]
            print(round(totalc,2))

    elif choice == 4:
        print("Delete Item:\nSearch by\n1\tName\n2\tUid\n3\tExit Deletion")
        n = int(input("Deletion mode: "))

        if n ==1:
            name = str(input("Enter Item Name: "))
            unwanted = None

            for uid in carts:
                if carts[uid]["Name"] == name:
                    unwanted = uid
                    break

            if unwanted is not None:
                del carts[unwanted]
                print("Item Deleted Successfully!")
            else:
                print("Item not found!")

        elif n ==2:
            dUid = int(input("Enter Item Uid: "))
            if dUid in carts:
                del carts[dUid]
                print("Item Deleted Successfully!")
            else:
                print("Error! Item matching UID does not Exist!")

        elif n == 3:
            print("Deletion Skipped!")
        else:
            print("Invalid Choice!!")  

    elif choice == 5:
        flag = False
        print("Exiting Program...")
    else:
        print("Invalid Choice!")