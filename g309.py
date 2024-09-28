n, k=map(int, input().split())
tree=[]
cake=[0]*n
cake[0]=k
for i in range(n):
    s=list(map(int, input().split()))[1:]
    tree.append((s))

queue=[0]
while queue:
    node=queue.pop(0)
    deg=0
    tmp=[]
    for i in tree[node]:
        if i!=-1:
            deg+=1
            tmp.append(i)
            queue.append(i)
            
    if deg!=0:
        ave=cake[node]//(deg+1)
        for i in tmp:
            cake[i]=ave
        cake[node]-=ave*deg

print(*cake)