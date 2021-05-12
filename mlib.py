import matplotlib.pyplot as plt

x_axes=[1,2,3,4,5,6,7]
y_axes=[x**2 for x in x_axes]
plt.style.use('seaborn')
fig,ax=plt.subplots()
ax.plot(x_axes,y_axes,linewidth=3)
ax.scatter(x_axes,y_axes,100)
plt.show()

