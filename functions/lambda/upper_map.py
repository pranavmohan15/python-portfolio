list1=[]
num=int(input("enter the limit:"))
for i in range(num):
    v=input("enter the values:")
    list1.append(v)
a=map(lambda i:i.upper(),list1)
print(list(a))