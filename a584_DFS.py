g={}
for _ in range(int(input())):
    s=input().split()
    n=s.pop(0)
    if n not in g:
        g[n]=s
    else:
        g[n]+=s
    for i in s:
        if i not in g:
            g[i]=[n]
        else:
            g[i]+=[n]

d=0
distance={}
visited=[]
def dfs(x,d):
    visited.append(x)
    distance[x]=d
    for i in g[x]:
        if i not in visited:
            dfs(i,d+1)

a,b=input().split()
dfs(a,d)
print(distance[b])