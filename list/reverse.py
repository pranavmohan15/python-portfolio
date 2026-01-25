n=int(input("enter the number of items:"))
list1=[]
rev_list=[]
for i in range(n):
    item=int(input("enter the item:"))
    list1.append(item)
    rev_list.insert(0,item)
print(list1)
print("reverse list is ",rev_list)