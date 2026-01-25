# Find frequency of each character
a=input("enter the string:")
ac=''
for i in a:
    if i not in ac:
        c=0
        for j in a:
            if j==i:
                c+=1
        print(i,"in the given string",c,"times")
    ac+=i

