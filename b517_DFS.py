def dfs(x):
    visited.append(x)
    for i in g[x]:
        if i not in visited:
            dfs(i)

for _ in range(int(input())):
    data=[]
    g={}
    s=input().split()
    node=[]
    cnt=0
    while s:
        a,b=s.pop(0).split(',')
        a=int(a)
        b=int(b)
        node.append(a)
        node.append(b)
        if a not in g:
            g[a]=[b]
        else:
            g[a]+=[b]
        if b not in g:
            g[b]=[a]
        else:
            g[b]+=[a]
        cnt+=1
        
    node=list(set(node))
    if len(set(node))!=cnt+1:
        print('F')
    else:
        visited=[]
        dfs(node[0])
        if sorted(visited)!=sorted(node):
            print('F')
        else:
            print('T')