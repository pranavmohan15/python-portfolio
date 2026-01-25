import pandas as pd
# a={
#     'data':[1,2,3,4],
#     'value':['one','two','thr','fou']
# }
# b=pd.DataFrame(a)
# print(b.to_string(index=False))

# a={
#     ' Title':['name','age',' course'],
#      'Data':[' pranav',23,' python'],
#      'demo':[1,2,7]

# }
# b=pd.DataFrame(a)
# print(b.to_string(index=False))

#in dictionary keys are column names

#in tuple input is a list of tuple each row is a list of tuple

# read the data in tuple 
a=[(1,'pranav',50),
   (2,'pm',49),
   (3,'pranav m',45)
   ]
b=pd.DataFrame(a,columns=['rollno','name','mark'])
print(b.to_string(index=False))