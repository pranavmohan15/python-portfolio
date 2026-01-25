item=[1,2,3]
for x in range(3):
    try:
        indx=int(input("enter the index number:"))
        print(item[indx])
        break
    except IndexError:
        print("index out of range")
        break

