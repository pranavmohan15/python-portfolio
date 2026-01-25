def pass_fail(a):
    if a>=40:
        return "Pass"
    else:
        return "Fail"
a=int(input("enter the mark:"))
print(pass_fail(a))