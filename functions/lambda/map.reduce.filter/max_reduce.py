from functools import reduce
list1= [5, 8, 3, 15, 2]
max=reduce(lambda a,b:a if a>b else b,list1)
print(max)