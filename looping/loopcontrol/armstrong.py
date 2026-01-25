num= int(input("Enter a number: "))
temp= num
sum = 0
n = len(str(num))

while 0<num:
    digit = num % 10         
    sum += digit ** n  
    num //= 10               

if sum == temp:
    print("it is an Armstrong number")
else:
    print("it is not an Armstrong number")
