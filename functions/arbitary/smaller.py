def smallest_list(*n):
    smallest=n[0]
    for i in n:
        if i<smallest:
            smallest=i
    return smallest
l=[]
num=int(input("enter the number of elements:"))
for i in range(num):
    v=int(input("enter the values:"))
    l.append(v)
print(smallest_list(*l))

