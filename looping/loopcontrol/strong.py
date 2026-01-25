num = int(input("Enter a number: "))
temp = num
sum = 0

while temp > 0:
    digit = temp % 10   
    fact = 1
    i = 1
    while i <= digit:     
        fact *= i
        i += 1
    sum += fact
    temp //= 10            

if sum == num:
    print(f"{num} is a Strong number")
else:
    print(f"{num} is not a Strong number")
