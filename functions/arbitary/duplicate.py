def duplicate(*n):
    list2=[]
    for i in n:
        if i not in list2:
            list2.append(i)
    return list2
list1=[]
num=int(input("enter the limit:"))
for i in range(num):
    v=int(input("enter the value:"))
    list1.append(v)
print(duplicate(*list1))
