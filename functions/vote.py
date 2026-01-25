def vote(age):
    if age<18:
        print("not eligible to vote")
    elif age>18 and age<40:
        print("Young voter")
    elif age>40 and age<60:
        print("Middle-aged voter")
    elif age>60:
        print("senior voter")
age=int(input("enter the age:"))
vote(age)