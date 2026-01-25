n=int(input("enter the number of elements:"))
list1=[]
for i in range(n):
    item=int(input("enter the item:"))
    list1.append(item)
print(list1)
largest=list1[0]

for i in list1:
    if i>largest:
        largest=i
print("largest is",largest)