n=1
while n<=100:
    if n%3==0 and n%5==0:
        print(f"{n} is the smallest number divided by both 3 and 5")
        break
    n+=1