import heapq
for _ in range(int(input())):
    n=int(input())
    m=int(input())
    G=[]
    for i in range(n):
        s=['#']+list(map(int, input().split()))+['#']
        G.append(s)
    G.insert(0,['#']*(m+2))
    G.append(['#']*(m+2))
    dx=(0,0,1,-1)
    dy=(1,-1,0,0)
    queue=[(G[1][1],1,1)]
    while queue!=[]:
        pair=heapq.heappop(queue)
        num=pair[0]
        y=pair[1]
        x=pair[2]
        for i in range(4):
            r=dy[i]+y
            c=dx[i]+x
            if G[r][c]=='#' or G[r][c]<0:
                continue
            G[r][c]=-num-G[r][c]
            heapq.heappush(queue, (abs(G[r][c]),r,c))

    print(abs(G[-2][-2]))