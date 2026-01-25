num1=float(input("enter the first number : "))
num2=float(input("enter the second number : "))
operator=input("enter the operator (+,-,*,/): ")
if operator=="+":
    print("the sum is : ",num1+num2)
elif operator=="-":
    print("the difference  : ",num1-num2)
elif operator=="*":
    print("the product is : ",num1*num2)
elif operator=="/":
    print("the quotient is : ",num1/num2)
else:
    print("invalid operator")