def vote_check(a):
    if a>=18:
        print("eligible for vote")
    else:
        print("not eligible")

a=int(input("enter the age:"))
vote_check(a)