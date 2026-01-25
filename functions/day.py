def week(a):
    if a==1:
        print("sunday")
    elif a==2:
        print("monday")
    elif a==3:
        print("tuesday")
    elif a==4:
        print("wednesday")
    elif a==5:
        print("thursday")
    elif a==6:
        print("friday")
    elif a==7:
        print("saturday")
    else:
        print("enter a number between 1-7")
a=int(input("enter a number bw 1-7:"))
week(a)