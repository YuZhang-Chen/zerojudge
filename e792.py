def dfs(v):
    visited[v]=1
    for i in path[v]:
        if visited[i]==0:
            dfs(i)

n,m,q=map(int, input().split())
path=[[] for i in range(n)]

for i in range(m):
    a,b=map(int, input().split())
    path[a].append(b)

for i in range(q):
    a,b=map(int, input().split())
    visited=[0 for i in range(n+1)]
    dfs(a)
    if visited[b]==1:
        print('YES')
    else:
        print('NO')