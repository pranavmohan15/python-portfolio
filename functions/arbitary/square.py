def square_list(*n):
    square=[]
    for i in n:
        square.append(i*i)
    return square
list1=[]
n=int(input("enter the limit:"))
for i in range(n):
    v=int(input("enter the values:"))
    list1.append(v)
print(square_list(*list1))
        