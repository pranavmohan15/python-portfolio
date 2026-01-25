def greater(*n):
    greater=[]
    for i in n:
        if i>10:
            greater.append(i)
    return greater
            
l=[]
num=int(input("enter the limit:"))
for i in range(num):
    v=int(input("enter the values:"))
    l.append(v)
print(greater(*l))
