text=input("enter the paragraph:")
text=text.lower()
# print(text)
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
new_text=""
for i in text:
    if i not in punctuations:
        new_text+=i
word=new_text.split()
# print(word)
f={}
for i in word:
    if i in f:
        f[i]+=1
    else:
        f[i]=1
print("frequency count")
# print(f)
for i,j in f.items():
    print(i,":",j)
