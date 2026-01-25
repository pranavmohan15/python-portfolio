def multi_list(*n):
    multi=1
    for i in n:
        multi*=i
    return f"the result is {multi}"
list1=[]
num=int(input("enter the limit:"))
for i in range(num):
    v=int(input("enter the value:"))
    list1.append(v)
print(list1)
print(multi_list(*list1))