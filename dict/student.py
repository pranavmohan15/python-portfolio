std={}
sum=0
for i in range(2):
    name=input("enter the name:")
    marks=int(input("enter the marks:"))
    sum+=marks
    std[name]=marks

highest=max(std,key=std.get)
print("the highest scored student is",highest)

lowest=min(std,key=std.get)
print("the lowest scored student is",lowest)

average=sum/len(std)
# average = sum(std.values()) / len(std)
print("average is",average)

g=input("enter the name:")
if g in std:
    new_marks=int(input("enter the new marks of the student:"))
    std[g]=new_marks
else:
    print("the student is not exist")
#std.update({"pranav":90})
print(std)
print("the descending order in the basis of marks",sorted(std,key=std.get,reverse=True))