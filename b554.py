def dfs(x,y):
    ret=0
    g[x][y]=0
    for i in range(4):
        if g[x+d[i][0]][y+d[i][1]]==1:
            ret=max(ret, dfs(x+d[i][0],y+d[i][1]))
    g[x][y]=1
    return ret+1

d=((1,0),(-1,0),(0,1),(0,-1))
g=[]
n=int(input())
for i in range(n):
    g.append([])
    s=[0]+list(input())+[0]
    for j in range(n+2):
        g[i].append(int(s[j]))
g.insert(0, [0]*(n+2))
g.append([0]*(n+2))

if g[1][1]==0:
    print(0)
else:
    ans=dfs(1,1)
    print(ans)