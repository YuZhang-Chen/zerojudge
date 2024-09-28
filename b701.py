x,y=map(int, input().split())
g=[]
for _ in range(x):
    g.append(list(map(int, input().split())))

dxy=[(0,1),(1,0),(0,-1),(-1,0)]

for i in range(x):
    for j in range(y):
        if g[i][j]==1:
            g[i][j]=2
            pre=[1e9,1e9,-1e9,-1e9]
            q=[(i,j)]
            cnt=0
            while q:
                r,c=q.pop(0)
                cnt+=1
                g[r][c]=2
                if c<pre[0]:
                    pre[0]=c
                if r<pre[1]:
                    pre[1]=r
                if c>pre[2]:
                    pre[2]=c
                if r>pre[3]:
                    pre[3]=r

                for aa in range(4):
                    newr,newc=r+dxy[aa][0],c+dxy[aa][1]
                    if newr<0 or newr>=x or newc<0 or newc>=y:
                        continue
                    if g[newr][newc]==1 and (newr,newc) not in q:
                        q.append((newr,newc))
            print(*pre, end=' ')
            print(cnt)
