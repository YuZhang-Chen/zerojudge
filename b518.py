for _ in range(int(input())):
    m=int(input())
    parent=[-1]*m
    deg=[0]*m
    for i in range(m):
        a, b=map(int, input().split(","))
        if b==99:
            continue
        parent[a]=b
        deg[b]+=1

    if _>0:
        print()

    for i in range(len(deg)):
        if deg[i]==0:
            node=i
            path=[]
            while node!=-1:
                path.append(node)
                node=parent[node]
            if len(path)>2:
                path=str(path[1:-1]).replace("[", "{").replace("]", "}")\
                .replace(" ", "")
            else:
                path="N"
        
            print("%d:%s"%(i, path))