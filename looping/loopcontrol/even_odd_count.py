n=int(input("enter a number : "))
even_count=0
odd_count=0
while n!=0:
    if n%2==0:
        even_count+=1
    else:
        odd_count+=1
    n=n//10
print("even digits",even_count)
print("odd digits",odd_count)