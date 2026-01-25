n=int(input("enter a number : "))
rev=0
temp=n
while n!=0:
    rem=n%10
    rev=rev*10+rem
    n=n//10
if(temp==rev):
    print("it is pallindrome")
else:
    print("it is not pallindorme")
    
