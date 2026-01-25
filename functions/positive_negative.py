def positive_negative(a):
    if a>0:
        return "positive"
    elif a<0:
        return "negative"
    else:
         return "zero"
a=int(input("enter the number:"))
print(positive_negative(a))