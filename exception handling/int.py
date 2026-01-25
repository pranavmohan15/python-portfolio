values=["10","20","abc","40"]
for x in values:
    try:
        nums=int(x)
        print(f"{x} is valid")
    except ValueError:
        print(f"{x} is invalid")
    finally:
        print("all set")