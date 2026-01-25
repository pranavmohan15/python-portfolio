num = int(input("enter a number: "))
total = 0

while num > 0:
    total += num % 10
    num //= 10

print( "the total sum of digits is",total)
