import matplotlib.pyplot as plt

#part of the figure
slices=[50,20,20,10]
#labales of the figure
l=['food','rent','shopping','extra']
#color
c=['red','green','orange','blue']
plt.pie(slices,labels=l,colors=c)
plt.title('Expense')
plt.show()