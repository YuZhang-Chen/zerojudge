while 1:
    n,m=map(int, input().split())
    if n==0 and m==0:
        break
    g=[]
    for i in range(n):
        g.append(list(input()))

    dxy=[(0,1),(1,0),(0,-1),(-1,0),(-1,1),(-1,-1),(1,1),(1,-1)]
    cnt=0
    for i in range(n):
        for j in range(m):
            if g[i][j]=='@':
                cnt+=1
                q=[(i,j)]
                while q:
                    y,x=q.pop(0)
                    for r,c in dxy:
                        newr=y+r
                        newc=x+c
                        if 0<=newr<n and 0<=newc<m and g[newr][newc]=='@':
                            g[newr][newc]='*'
                            q.append((newr,newc))
    print(cnt)