# n=int(input("enter the number of elements:"))
# list1=[]
# sum=0
# for i in range(n):
#     item=int(input("enter the item:"))
#     list1.append(item)
# print("list of elemnts",list1)
# for i in list1:
#     sum+=i
# print("sum of items in a list",sum)

n=int(input("enter the number of elements:"))
list1=[]

sum=0
for i in range(n):
    item=int(input("enter the item:"))
    list1.append(item)
print(list1)
for i in list1:
    sum+=i
print("the sum of elemnts:",sum)