#Check if a string is a palindrome
a=input("enter a string:")
# b=a[::-1]
r=''
for i in a:
    r=i+r
if a==r:
    print("it is pallindrome")
else:
    print("not pallindrome")