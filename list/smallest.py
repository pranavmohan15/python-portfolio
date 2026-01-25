n=int(input("enter the number of elements: "))
list1=[]
for i in range(n):
    item=int(input("enter the elements:"))
    list1.append(item)
print(list1)
smallest=list1[0]
for i in list1:
    if i<smallest:
        smallest=i
print("smallest number is ",smallest)