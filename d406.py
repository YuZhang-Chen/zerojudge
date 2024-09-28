cnt=0
while True:
    try:
        cnt+=1
        s=int(input())
        n, m=map(int, input().split())
        g=[]
        for _ in range(n):
            g.append(list(map(int, input().split())))

        dxy=[(0, 1), (1, 0), (0, -1), (-1, 0)]
        if s==2:
            dxy=dxy[:-1]

        start_c=g[0].index(1)
        queue=[(0, start_c)]
        while len(queue)>0:
            r, c=queue.pop(0)
            for a, b in dxy:
                newr=r+a
                newc=c+b
                if 0<=newr<n and 0<=newc<m:
                    if g[newr][newc]==1:
                        queue.append((newr, newc))
                        g[newr][newc]=g[r][c]+1
        g[0][start_c]=1
        
        print("Case %d:"%(cnt))
        print(*g[0])
        for i in g[1:]:
            arr=[]
            for j in i:
                arr.append(0 if j==1 else j)
            print(*arr)
    except:
        break