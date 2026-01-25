#union()-it creates new set..never modify the exisitng one
a={1,2,3,4,5}
b={4,5,6,7}
# c=a.union(b)
# print(c)

#update()-modifies the original set
# a.update(b)
# print(a)

#intersection_update()-it keeps only the common elemnts in the two sets
# a.intersection_update(b)
# print(a)

#intersection-it return a new set that contain the common elemets
# c=a.intersection(b)
# print(c)

#symmetric_difference_update()-keep all,but not the duplicates,it return only the unique elements
# a.symmetric_difference_update(b)
# print(a)

#symmetric_difference()-keep all,but not the duplicates,it returns the elemnts in a new set 
c=a.symmetric_difference(b)
print(c)