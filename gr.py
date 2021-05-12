way=[[]]
graph=dict()
visited=[]
not_vis=['S','A','B','C','G']
graph['S']=['A','B']
graph['A']=['B','C']
graph['B']=['C']
graph['C']=['G']
graph['G']=[]
w=0
start_point='S'
not_vis.remove(start_point)
visited.append(start_point)
p_p=start_point
n_p=graph[p_p[0]]
while n_p!='G':
    visited.append(n_p)
    p_p=n_p
    not_vis.remove(p_p)


print(visited)
