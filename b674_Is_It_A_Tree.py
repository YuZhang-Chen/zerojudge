while 1:
    n=int(input())
    if n==0:
        break
    g={}
    node=set(); root=set(); t=set()
    s=list(map(int, input().split()))
    for i in range(0, len(s),2):
        node.add(s[i])
        node.add(s[i+1])
        t.add(s[i+1])
        root.add(s[i])
        if s[i] not in g:
            g[s[i]]=[s[i+1]]
        else:
            g[s[i]]+=[s[i+1]]
        if s[i+1] not in g:
            g[s[i+1]]=[]

    Is_tree=True
    root=list(root-(root&t))
    if len(root)==0:
        Is_tree=False
    else:
        root=root[0]

    if Is_tree:
        visited=[]
        visited.append(root)
        cnt=0
        def dfs(x):
            global Is_tree,cnt
            for i in g[x]:
                if i not in visited:
                    visited.append(i) 
                    cnt+=1
                    dfs(i)
                else:
                    Is_tree=False
        dfs(root)

    if len(node)-1!=cnt:
        Is_tree=False

    if Is_tree:
        print('y')
    else:
        print('n')