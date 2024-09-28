t=int(input())
for xx in range(t):
    print('Case %d:'%(xx+1))
    n=int(input())
    adj=[]
    for _ in range(n):
        s=list(map(int, input().split(', ')))
        adj.append(s)

    data=[]
    for i in range(len(adj)):
        for j in range(len(adj[i])):
            if adj[i][j]!=0:
                data.append((i,j,adj[i][j]))

    parent=[i for i in range(n)]
    data.sort(key=lambda x:x[2])

    for a,b,c in data:
        if parent[a]==parent[b]:
            continue
        print('%s-%s %d'%(chr(a+65),chr(b+65),c))
        mx=max(parent[a],parent[b])
        mn=min(parent[a],parent[b])
        for i in range(len(parent)):
            if parent[i]==mn:
                parent[i]=mx