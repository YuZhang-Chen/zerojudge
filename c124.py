while True:
    L, R, C=map(int, input().split())
    if L==0 and R==0 and C==0:
        break
    g=[]
    for i in range(L):
        g2=[]
        for j in range(R):
            s=list(input())
            arr=[]
            for k in range(C):
                if s[k]=="S":
                    start=(i, j, k)
                if s[k]=="E":
                    stop=(i, j, k)
                arr.append(0 if s[k]=="." else "#")
            g2.append(arr)
        g.append(g2)
        input()

    i, j, k=start
    g[i][j][k]=0
    i, j, k=stop
    g[i][j][k]=0
    
    dxyz=((0, 1, 0), (0, -1, 0), (1, 0, 0),
        (-1, 0, 0), (0, 0, 1), (0, 0, -1))
    queue=[start]
    while queue:
        l, r, c=queue.pop(0)
        for i, j, k in dxyz:
            newL=l+i
            newR=r+j
            newC=c+k
            if 0<=newL<L and 0<=newR<R and 0<=newC<C:
                if g[newL][newR][newC]==0:
                    queue.append((newL, newR, newC))
                    g[newL][newR][newC]=g[l][r][c]+1

    i, j, k=stop
    if g[i][j][k]==0:
        print("Trapped!")
    else:
        print("Escaped in %d minute(s)."%(g[i][j][k]))