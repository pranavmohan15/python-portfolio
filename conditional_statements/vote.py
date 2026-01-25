age=int(input("enter your age: "))
if age<18:
    print("you are not eligible to vote")
elif age>=18 and age<=40:
    print("young voter")
elif age>40 and age<=60:
    print("middle aged  voter")
elif age>60:
    print("senior voter")