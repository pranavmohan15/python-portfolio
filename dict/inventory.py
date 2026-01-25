inventory={"pen":20, "pencil":50,"notebook":30
}
while True:
        print("INVENTORY MANAGEMENT SYSTEM")
        print("1.add new item with quantity")
        print("2.update quantity of existing item")
        print("3.Remove an item when out of stock")
        print("4.Display all items with quantites")
        print("5.find total number of items in the store")


        choice=input("enter your choice(1-6):")

        if choice == '1':
            item=input("Enter  item name:")
            qty=int(input("enter quantity: "))
            inventory.update({item:qty})
            print(inventory)
        elif choice=='2':
            item=input("Enter name to update:")
            if item in inventory:
                qty=int(input("enter new quantity: "))
                inventory[item]=qty
                print(inventory)
            else:
                print("item not found")
        elif choice=='3':
            item=input("Enter item name to check/remove:")
            if item in inventory:
                if inventory[item]==0:
                    inventory.pop(item)
                    print(inventory)
                else:
                    print(f"{item} in stock")
            else:
                print("not found")
        elif choice =='4':
            print("\nItem\tQuantity")
            print("------------------")
            for key, value in inventory.items():
                print(f"{key}\t{value}")


        elif choice =='5':
            total=sum(inventory.values())
            print(f"total number of items in store:{total}")
        elif choice =='6':
            break
        else:
            print("enter a valid option")
