n=int(input("enter the number of elements:"))
list1=[]
for i in range(n):
    item=int(input("enter the elements:"))
    list1.append(item)
print(list1)
list2=[]
for i in list1:
    if i not in list2:
        count=0
        for j in list1:
            if j==i:
             count+=1
        print(i,"in the given list",count,"times")
    list2.append(i)

