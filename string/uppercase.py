# Count uppercase letters
a=input("enter the string: ")
count=0
for i in a:
    if 'A'<=i<='Z':
        count+=1
print("the number of uppercase  in a given string is",count)