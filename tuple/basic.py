#this is the way of writing tuple
# a=25,
# a=(25,)
# print(type(a))
a=int(input("enter the number of elements:"))
b=[]
for i in range(a):
    item=int(input("enter the item:"))
    b.append(item)
print(tuple(b))