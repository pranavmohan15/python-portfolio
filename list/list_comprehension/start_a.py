# list1=[]
# num=int(input("enter the limit:"))
# for i in range(num):
#     v=input("enter the string:")
#     list1.append(v)
# s=[i for i in list1 if i[0].lower()=='a']
# print(s)

n=int(input("enter the limit:"))
list1=[]
for i in range(n):
    item=input("enter the item:")
    list1.append(item)
s=[i for i in list1 if i[0].lower()=='a']
print(s)
