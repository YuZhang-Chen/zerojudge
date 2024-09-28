n,m=map(int, input().split())
path=[[] for i in range(n)]
s=int(input())
for _ in range(m):
    a,b=map(int, input().split())
    path[a].append(b)

distance=[0 for i in range(n)]
q=[(s,0)]
visited=[s]
while q:
    pos,d=q.pop(0)
    for i in path[pos]:
        if i not in visited:
            visited.append(i)
            q.append((i,d+1))
            distance[i]=d+1
print(len(visited)-1)
print(sum(distance))