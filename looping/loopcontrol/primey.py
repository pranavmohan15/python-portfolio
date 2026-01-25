n=int(input("enter a number : "))
i=2
if n<=1:
    print("it is not a prime number")
else:
    while i<n:
        if n%i==0:
            print("it is not prime number")
            break
        i+=1 
    else:
        print("it is prime number")
       

 