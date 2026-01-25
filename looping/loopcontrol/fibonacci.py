n=int(input("Enter the limit: "))
a,b=0,1
count=0
if n<=0:
    print("enter a positive number")
elif n==1:
    print("the sequence up to: ",n)
    print(a)
else:
    print("Fibonacci Sequence is: ")
    while count<n:
        print(a, end=' ')
        c=a+b
        a=b
        b=c
        count+=1
print()