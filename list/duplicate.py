# n=int(input("enter the number of elements:"))
# list1=[]
# for i in range(n):
#     item=int(input("enter the element:"))
#     list1.append(item)
# print("the list is",list1)
# list2=[]
# for i in list1:
#     if i not in list2:
#         list2.append(i)
# print("the list after remove the duplicates",list2)

n=int(input("enter the number of elements:"))
list1=[]
list2=[]
for i in range(n):
    item=int(input("enter the item:"))
    list1.append(item)
print(list1)
for i in list1:
    if i not in list2:
        list2.append(i)
print("list without duplicate elements",list2)