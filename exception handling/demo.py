try:
    a=int(input('Enter 1st number '))
    b=int(input('Enter 2nd number '))
    c=a/b
except ZeroDivisionError:
    print('zero division error')
except ValueError:
    print('value error plaese input correct data')
else:
    print(c)
finally:
    print('hiiiiiii')

