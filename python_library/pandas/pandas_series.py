import pandas as pd
import numpy as np

#create array
a=np.array([1,2,3])

#create a series
#normal series with index 0-len(a)
#b=pd.series(a)

b=pd.Series(a,index=['x','y','z']) #create x,y,z index
print(b)

print(b['y'])