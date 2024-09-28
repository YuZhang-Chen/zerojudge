dir_rc=((0, 1), (1, 0), (0, -1), (-1, 0))
def dfs(row, col):
    global cnt
    cnt+=1
    g[row][col]=water
    for i, j in dir_rc:
        newr=row+i
        newc=col+j
        if g[newr%n][newc%m]==land:
            dfs(newr%n, newc%m)

while True:
    try:
        n, m=map(int, input().split())
        g=[]
        for _ in range(n):
            s=list(input())
            g.append(s)

        x, y=map(int, input().split())
        land="w" if g[x][y]=="w" else "l"
        water="w" if land=="l" else "l"
        cnt=0
        dfs(x, y)
        ans=-1
        for i in range(n):
            for j in range(m):
                if g[i][j]==land:
                    cnt=0
                    dfs(i, j)
                    if cnt>ans:
                        ans=cnt
                        cnt=0
        print(ans)
        input()
    except EOFError:
        break