d={
    'name':'pranav',
    8:90,
    (90,8):"hi"

}
# print(len(d))--it is used to find the length of the dictionary


#access elements
#1.var['key']-- it displays the exists value in the specific key
# print(d['name'])
# 2. var.get('key')--here dont show error when if there is no key in that name
print(d.get(8))
# 3. var.keys()--display all keys
# print(d.keys())
# 4. var.values() -- display all values
# print(d.values())
# 5.var.items()--display items as list of tuples
# print(d.items())#its type is dict items
# print(d) #its type is dict


#check if a key in dictionary,if it exists gives true otherwise gives false
# print('name' in d)

#add elements
# var['key']=value---if it an exisitng key it will update
# d['place']='cheemeni'
# print(d)

#update()-used to add more than one pair of items
# d.update({'address':"kizh",'phn':86475})
# print(d)

#remove items
# 1.pop()--remove specific key
# d.pop('name')

# 2.popitem()--remove the last pair
# d.popitem()

# 3.clear()--clear all
# d.clear()


# 4.del delete the entire dict
