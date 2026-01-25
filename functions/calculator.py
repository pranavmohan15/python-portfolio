def cal(a,oper,b):
    if oper=='+':
        print(a+b)
    elif oper=='-':
        print(a-b)
    elif oper=='/':
        print(a/b)
    elif oper=='*':
        print(a*b)
    else:
        print("enter a valid operator")

a=int(input("enter the first number:"))
b=int(input("enter the second number:"))
oper=input("enter an operator between(+,*,/,-):")
cal(a,oper,b)