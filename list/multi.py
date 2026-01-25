n=int(input("enter the number of elements:"))
list1=[]
for i in range(n):
    item=int(input("enter the item:"))
    list1.append(item)
print(list1)
multi=1
for i in list1:
    multi*=i
print("multiplication of elements in a list",multi)
