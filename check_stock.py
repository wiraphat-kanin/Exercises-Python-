print("Inventory Management")
print("1.Check Stock \n2.Receive Product \n3.Deliver Product \n4.Exit")
stock = int(input("Current Stock "))
while stock >0:
    choice = int(input("Select menu : "))

    if 1 <= choice <= 4 :
        if choice == 1:
            print(f"Stock : {stock}")
        elif choice == 2:
            receive = int(input("Receive Product : "))
            if receive <= 0:
                while True:
                    receive = int(input("Enter Receive Product Again : "))
                    stock += receive
                    if receive > 0:
                        break
            else :
                stock += receive
        elif choice == 3:

            deliver = int(input("Receive Product : "))
            if deliver <= 0:
                while True:
                    deliver = int(input("Enter Receive Product Again : "))
                    stock -= deliver
                    if deliver > 0:
                        break
            else :
                stock -= deliver

        elif choice == 4:
            print("Exiting the program")
            break

    else:
        print("This item does not exist. Please enter the required item. \n")