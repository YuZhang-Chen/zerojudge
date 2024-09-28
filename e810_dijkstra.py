n,m=map(int, input().split())
path=[[] for i in range(n)]
for _ in range(m):
    a,b,w=map(int, input().split())
    path[a].append((b,w))
    path[b].append((a,w))

a,b=map(int, input().split())
INF=1e9
distance=[INF for i in range(0,n)]
distance[a]=0
q=[a]
while q:
    pos=q.pop(0)
    for node,d in path[pos]:
        p=max(distance[pos], d)
        if p<distance[node]:
            distance[node]=p
            q.append(node)

if distance[b]==INF:
    print(-1)
else:
    print(distance[b])