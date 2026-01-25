import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
products=[]
sales=[]
n=int(input("enter the number of prodcuts:"))
for i in range(n):
    name=input(f'enter the naem of the {i+1} prodcut name:')
    qty=int(input(f'enter the weekly saels of {name}:'))
    products.append(name)
    sales.append(qty)

df=pd.DataFrame(
    {
        'products':products,
        'weekly_sales':sales
    }

)
sales_ary=np.array(sales)
total_sales=np.sum(sales_ary)
best_selling_product=products[np.argmax(sales_ary)]
max_values=np.max(sales_ary)

print("Total weekly sales:", total_sales)
print("Best selling product:", best_selling_product)
print("Highest sales value:", max_values)

plt.bar(df['products'],df['weekly_sales'])
plt.title('weekly sales details')
plt.xlabel("products")
plt.ylabel("sales count")
plt.show()

plt.pie(df['weekly_sales'],labels=df['products'])
plt.title('sales details in chart')
plt.show()