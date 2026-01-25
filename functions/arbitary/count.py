def count_list(*n):
    odd_count=0
    even_count=0
    for i in n:
        if i%2==0:
            even_count+=1
            
        else:
            odd_count+=1
    
    return f"oddcount={odd_count} and evencount={even_count}"
l=[]
num=int(input("enter the limit:"))
for i in range(num):
    v=int(input("enter the values:"))
    l.append(v)
print(count_list(*l))

