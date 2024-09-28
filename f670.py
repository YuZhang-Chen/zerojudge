n,m=map(int, input().split())
parent=[int(i) for i in range(n+1)]
for _ in range(m):
    a,b=map(int, input().split())
    if a>b:
        a,b=b,a
    mx=max(parent[a],parent[b])
    mn=min(parent[a],parent[b])
    for i in range(len(parent)):
        if parent[i]==parent[mn]:
            parent[i]=parent[mx]
print(len(set(parent))-1)