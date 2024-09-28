def dfs(x, p):
    visited[x]=1
    for i in range(81):
        if tree[x][i]==1 and i!=p and visited[i]!=1:
            dfs(i, x)

for _ in range(int(input())):
    s=input().split()
    node=[0]*81
    tree=[[0 for _ in range(81)] for _ in range(81)]
    root=None
    edge=0
    for i in s:
        a, b=list(map(int, i.split(",")))
        if root==None:
            root=a
        node[a]=1
        node[b]=1
        tree[a][b]=1
        tree[b][a]=1
        edge+=1

    visited=[0]*81
    dfs(root, root)
    len_node=node.count(1)
    v_node=visited.count(1)
    
    is_tree=True
    if len_node-1!=edge or len_node!=v_node:
        is_tree=False
    print("T" if is_tree else "F")