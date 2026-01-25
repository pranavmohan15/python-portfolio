def largest(a,b):
    if a>b:
        return a
    else:
        return b
a=int(input("enter the first number:"))
b=int(input("enter the second number:"))
print(f"{largest(a,b)} is the largest")
