def month(a):
    if a in [1,3,5,7,8,10,12]:
        print("the days in that month is 31")
    elif a==2:
        print("the days in that month is 28")
    elif a in [4,6,9,11]:
        print("the days in that month is 30")
    else:
        print("enter a valid number")
      
a=int(input("enter the number betweeen 1-12:"))
month(a)        