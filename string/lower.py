# Count lowercase letters
a=input("enter the string: ")
count=0
for i in a:
    if 'a'<=i<='z':
        count+=1
print("the number of lowercase  in a given string", count)