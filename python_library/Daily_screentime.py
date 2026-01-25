import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

apps=[]
minutes=[]
n=int(input("enter the number of apps:"))
for i in range(n):
    name=input(f"enter the name of {i+1} app:")
    time=int(input(f"enter the minutes used per day for {name}:"))
    apps.append(name)
    minutes.append(time)
df=pd.DataFrame(
    {
    "apps":apps,
    "minutes":minutes
    }
)
arr=np.array(minutes)
total_time=np.sum(arr)
highest_app=apps[np.argmax(arr)]
highest_time=np.max(arr)
lowest_app=apps[np.argmin(arr)]
lowest_time=np.min(arr)

print("TOTAL SCREEN TIME:",total_time)
print("HIGHEST USAGE APP AND ITS TIME:",highest_app,"-",highest_time)
print("LOWEST USAGE APP AND ITS TIME:",lowest_app,"-",lowest_time)

plt.bar(df['apps'],df['minutes'])
plt.title('Daily Screen Time Analyzer')
plt.xlabel("APPS")
plt.ylabel("MINUTES")
plt.show()

plt.pie(df['minutes'],labels=df['apps'])
plt.title('Daily Screen Time Analyzer')
plt.show()



