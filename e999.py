def dfs(x):
    global ans
    for i in g[x]:
        if i==n-1:
            ans+=1
        else:
            dfs(i)

n, e=map(int, input().split())
g=[[] for _ in range(n)]
for _ in range(e):
    a, b=map(int, input().split())
    g[a].append(b)
ans=0
dfs(0)
print(ans)