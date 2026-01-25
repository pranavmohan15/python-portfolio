nums=[10,5,0,2]
for x in nums:
    try:
        a=100/x
    except ZeroDivisionError:
        print("zero division error")
    else:
        print(a)
    # finally:
    #     print("all set")


