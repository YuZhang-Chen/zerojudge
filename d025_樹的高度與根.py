n=int(input())
parent=[-1 for i in range(n)]
deg=[0 for i in range(n)] #每個點的孩子數
h=[0 for i in range(n)]
for i in range(n):
    x=[int(a)-1 for a in input().split()]
    deg[i]=len(x)-1
    for j in range(1,len(x)):
        parent[x[j]]=i
q=[a for a in range(n) if deg[a]==0] #leaf
front=0 #索引值
root=parent.index(-1)

while front<len(q):
    v=q[front]
    front+=1
    p=parent[v]
    if p<0:
        break
    h[p]=max(h[p], h[v]+1)
    deg[p]-=1
    if deg[p]==0:
        q.append(p)

print(root+1)
print(sum(h))