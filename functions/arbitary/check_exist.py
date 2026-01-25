def check_exist(n,m):
    if m in n:
        print(f"{m} exist in the list")
    else:
        print(f"{m} is not in the list")
list1=[]
num=int(input("enter the limit:"))
for i in range(num):
    v=int(input("enter the value:"))
    list1.append(v)
print(list1)
m=int(input("enter the number to check:"))
check_exist(list1,m)
