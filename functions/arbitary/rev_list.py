def reverse(*a):
    rev_list=[]
    for i in a:
        rev_list.insert(0,i)
    return rev_list
l=[]
num=int(input("enter the limit:"))
for i in range(num):
    v=int(input("enter the value:"))
    l.append(v)
    
print(f" the reversed list is {reverse(*l)}")

    