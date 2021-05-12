from RandomWalk import RW

import matplotlib.pyplot as plt

fig,ax=plt.subplots()
RandomWalk = RW(5000)
RandomWalk.fill_walk()
points=range(5000)
ax.scatter(0,0,c='green',s=1000)
ax.scatter(RandomWalk.x_values[-1],RandomWalk.y_values[-1],c='green',s=1000)
ax.scatter(RandomWalk.x_values,RandomWalk.y_values,c=points,cmap=plt.cm.Blues,s=10)
fig2,ax2=plt.subplots(figsize=(10,6),dpi=5)
ax2.plot(RandomWalk.x_values,RandomWalk.y_values,linewidth=0.1,c='blue')
plt.show()

