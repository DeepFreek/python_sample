from kubik import KUB
from plotly.graph_objs import Bar,Layout
from plotly import offline
from matplotlib import pyplot
kubik=KUB(6)
roll_list=[]
count=10
mm=[]
for stepen in range(1,10):
    for i in range(1,count):
        kubik.roll()
        roll_list.append(kubik.num)
    print(roll_list)
    frequences=[0,0,0,0,0,0]
    for num in roll_list:
        frequences[num-1]+=1
    print(frequences)
    raznica=(max(frequences)-min(frequences))/count
    mm.append(raznica)
    count*=10
x_values=list(range(1,7))
data=[Bar(x=x_values,y=frequences)]
x_axis_config={'title':'Result'}
y_axis_config={'title':'frequency'}
my_layout=Layout(title='Res of rolling',xaxis=x_axis_config,yaxis=y_axis_config)
#offline.plot({'data':data,'layout':my_layout},filename='d6.html')
fig,ax=pyplot.subplots()
y_val=[10**x for x in range(1,10)]
ax.plot(y_val,mm,linewidth=5)
pyplot.show()
print(mm)

