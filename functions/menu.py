def menu(a):
    if a==1:
        print("pizza")
    elif a==2:
        print("Burger")
    elif a==3:
        print("pasta")
    else:
        print("enter a valid option")
print("1.pizz")
print("2.Burger")
print("3.Pasta")
a=int(input("enter a number:"))
menu(a)