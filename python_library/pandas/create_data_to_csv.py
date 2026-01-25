import pandas as pd
a=[(1,'pranav',23),
   (2,'pm',25),
   (3,'pranav m',21)
   ]
#create data frame
b=pd.DataFrame(a,columns=['rollno','name','mark'])

#add the data in csv format

b.to_csv('new.csv',index=False)

