# n=int(input("enter the number of elements: "))
# list1=[]
# for i in range(n):
#     item=int(input("enter the elements:"))
#     list1.append(item)
# print(list1)
# list2=[]
# for i in list1:
#     sqr=i**2
#     list2.append(sqr)
# print(list2)

n=int(input("enter the number of elements: "))
list1=[]
list2=[]
for i in range(n):
    item=int(input("enter the elements:"))
    list1.append(item)
    list2.append(item**2)
print(list1)
print(list2)