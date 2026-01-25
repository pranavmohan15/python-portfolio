# n = int(input("enter the number of elements: "))
# list1 = []

# for i in range(n):
#     item = int(input("enter the item: "))
#     list1.append(item)

# print(list1)

# m = int(input("enter the number to check: "))

# if m in list1:
#     print(f"{m} exists in this list")
# else:
#     print("not exist")


n=int(input("enter the limit:"))
list1=[]

for i in range(n):
    item=int(input("enter the item:"))
    list1.append(item)
print(list1)

m=int(input("entr the element to check:"))

if m in list1:
    print(f"{m} exists in the list")
else:
    print("it is not exist in the list")