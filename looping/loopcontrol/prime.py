n=int(input("enter a number : "))
i=2
if n<=1:
    print("it is not a prime number")
else:
    is_prime=True
    while i<=n//2:
        if n%i==0:
            is_prime=False
            break
        i+=1
if is_prime:
    print("it is prime number")
else:
    print("it is not prime number")


