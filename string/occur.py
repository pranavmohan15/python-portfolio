# Count occurrences of a given character
a=input("enter the string: ")
b=input("enter the char to check:")
count=0
for i in a:
    if i==b:
        count+=1
print(f"the occurence of {b} in the word {a} is {count} times")