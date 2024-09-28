n,m=map(int, input().split())
g=[]
min_num=1e9
for i in range(n):
    s=list(map(int, input().split()))
    g.append(s)
    mn=min(s)
    if mn<min_num:
        min_num=mn
        y=i
        x=g[i].index(min_num)

dxy=[(0,1),(1,0),(0,-1),(-1,0)]
q=[(y,x)]
path_sum=0
while q:
    r,c=q.pop(0)
    path_sum+=g[r][c]
    g[r][c]='#'
    lst=[]
    for a,b in dxy:
        newr=r+a
        newc=c+b
        if 0<=newr<n and 0<=newc<m and g[newr][newc]!='#':
            lst.append((g[newr][newc],newr,newc))
    if lst!=[]:
        lst.sort(key=lambda x:x[0])
        q.append((lst[0][1],lst[0][2]))

print(path_sum)
