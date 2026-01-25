n=int(input("enter the number of elements:"))
list1=[]
for i in range(n):
    item=int(input("enter the item: "))
    list1.append(item)
print(list1)
even_count=0
odd_count=0
for i in list1:
    if i%2==0:
        even_count+=1
    else:
        odd_count+=1
print("even number count",even_count)
print("odd number count ",odd_count)

