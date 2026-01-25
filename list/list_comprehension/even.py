# l=[]
# num=int(input("enter the limit:"))
# for i in range(num):
#     v=int(input("enter the values:"))
#     l.append(v)
# s=[i for i in l if i%2==0]
# print(s)

n=int(input("enter the limit:"))
l=[]
for i in range(n):
    item=int(input("enter the item:"))
    l.append(item)
print(l)
s=[i for i in l if i%2==0]
print(s)