a='pythonpy django'

# identity
# print(a is a)

#membership
# if 'p' in a:
#     print('yes')
# else:
#     print('no')

#print('z' in a)

# len()
# print(len(a)) :13

# for i in a:
#     print(i)

# for i in range(len(a)):
#     print(a[i])

# String Methods
# print(a.upper())
# print(a.lower())
# print(a.capitalize()) :only the first character of the entire string uppercase
# print(a.title()) :capitalize all the  first letter of the all words
# print(a.swapcase()) : small becomes big, big becomes small

# print(a.count('p')) : count of a char
# print(a.isalpha()) :check all are alphabets,if a space included with alphabets it returns false
# print(a.isnumeric()) :check if it is only numbers
# print(a.isalnum()) :check if they are mixing of numbers and alphbts
#print(a.split()) #here when we add space bw them,,it split by a ','
#print(a.replace('p','s'))
a="hi pranav mohan"
b=a.split()
print(b) #if we use string.split() it will give list