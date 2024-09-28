def dfs(graph,node,path=[]):
    path+=[node]
    for n in graph[node]:
        if n not in path:
            path=dfs(graph,n,path)
    return path

graph={'A':['B','C','D'],
    'B':['A','E'],
    'C':['A','F'],
    'D':['A','G','H'],
    'E':['B'],
    'F':['C','I','J'],
    'G':['D'],
    'H':['D'],
    'I':['F'],
    'J':['F']
}

print(dfs(graph, 'A'))