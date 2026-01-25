# Remove vowels from a string
a=input("enter  a string:")
result=""
for i in a:
    if i not in "aeiou":
        result+=i
print(result)