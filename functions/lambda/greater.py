l=[]
num=int(input("enter the limit:"))
for i in range(num):
    v=int(input("enter the values:"))
    l.append(v)
a=list(filter(lambda i:i>10,l))
print(a)