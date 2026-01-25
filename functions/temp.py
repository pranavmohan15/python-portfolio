def temp_check(temp):
    if temp>35:
        return "HOT"
    elif temp<35 and temp>=20:
        return "WARM"
    elif temp<20 and temp>=10:
        return "COOL"
    elif temp<10:
        return "COLD"
temp=int(input("enter your temp:"))
print(temp_check(temp))