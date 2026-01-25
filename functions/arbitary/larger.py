def larger_value(*n):
    largest=n[0]
    for i in n[1:]:
        if i>largest:
            largest=i
    return largest
l=[]
num=int(input("enter the number of items in the list:"))
for i in range(num):
    v=int(input("enter the value:"))
    l.append(v)
print(l)
print(f"{larger_value(*l)} is the largest value in the list")
    

