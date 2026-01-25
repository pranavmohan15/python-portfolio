def frequency(*n):
    list2=[]
    for i in n:
        if i not in list2:
            count=0
            for j in n:
                if j==i:
                    count+=1
            print(f"{i} in the given list {count} times")
        list2.append(i)
l=[]
num=int(input("enter the limit:"))
for i in range(num):
    v=int(input("enter the values:"))
    l.append(v)
print(l)
frequency(*l)
                
