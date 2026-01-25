n=int(input("enter the number of elements:"))
list1=[]
for i in range(n):
    item=int(input("enter the item:"))
    list1.append(item)
print(list1)
for i in list1:
    if i>10:
        print(f"{i} greater than ten")
    i+=1

