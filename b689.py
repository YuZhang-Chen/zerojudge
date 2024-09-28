n,m=map(int, input().split())
a=[]
for i in range(n):
    a.append([])
    s=['#']+list(input())+['#']
    for j in range(len(s)):
        if s[j]=='.':
            a[i].append(0)
        else:
            a[i].append('#')
a.insert(0, ['#']*(m+2))
a.append(['#']*(m+2))

for i in range(1,n+1):
    if i==0 or i==n:
        if 0 in a[i]:
            y=i
            x=a[i].index(0)
    else:
        if a[i][1]==0:
            y=i
            x=0
        if a[i][m]==0:
            y=i
            x=m
qy=[y]
qx=[x]
a[y][x]=1
dx=(0,0,1,-1)
dy=(1,-1,0,0)
while len(qy)>0:
    y=qy.pop(0)
    x=qx.pop(0)
    for i in range(4):
        r=y+dy[i]
        c=x+dx[i]
        if a[r][c]!='#' and a[r][c]==0:
            a[r][c]=a[y][x]+1
            qy.append(r)
            qx.append(c)
mx=[]
for i in range(1,n):
    for j in range(1,m):
        if a[i][j]!='#':
            mx.append(a[i][j])
mx=max(mx)
for i in range(1,n):
    for j in range(1,m):
        if a[i][j]==mx:
            ans=(i,j)
print(*ans)