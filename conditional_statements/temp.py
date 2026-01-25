temperature=float(input("Enter temperature in celsius: "))
if temperature>35:
    print("hot")
elif temperature>=20 and temperature<=35:
    print("warm")
elif temperature>=10 and temperature<20:
    print("cool")
elif temperature<10:
    print("cold")

