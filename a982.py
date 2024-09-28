g=[]
for _ in range(int(input())):
    s=input()
    arr=[]
    for i in s:
        if i=='.':
            arr.append(0)
        else:
            arr.append(i)
    g.append(arr)

dxy=[(0,1),(1,0),(-1,0),(0,-1)]
q=[(1,1)]
g[1][1]=1
while len(q)>0:
    aa=q.pop(0)
    y=aa[0]
    x=aa[1]
    for i in range(4):
        r=dxy[i][0]+y
        c=dxy[i][1]+x
        if g[r][c]!='#' and g[r][c]==0:
            q.append((r,c))
            g[r][c]=g[y][x]+1

if g[-2][-2]==0:
    print('No solution!')
else:
    print(g[-2][-2])