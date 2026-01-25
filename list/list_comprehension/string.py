list1=[]
num=int(input("enter the limit:"))
for i in range(num):
    v=input("enter the values:")
    list1.append(v)
print(list1)
s=[len(i) for i in list1]
print(s)