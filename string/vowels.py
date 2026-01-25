#Count vowels in a string
string=input("enter the string:")
#vw='aeiou'
vowel_count=0
for i in string:
    if i in 'aeiou':
   #if i in vw:
        vowel_count+=1
print("the count of vowels in a given string is",vowel_count)

