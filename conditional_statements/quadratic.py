#qudratic equation
a=float(input("Enter the value of a: "))
b=float(input("Enter the value of b: "))
c=float(input("Enter the value of c: "))
x=b**2-4*a*c
if x==0:
    x1=(-b)/(2*a)
    print(x1)
elif x>0:
    x2=(-b+x**0.5)/(2*a)
    x3=(-b-x**0.5)/(2*a)
    print(x2)   
    print(x3)
else:
    print("imaginary")

    
