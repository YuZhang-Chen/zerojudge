cnt=1
while True:
    n, m, q=map(int, input().split())
    if n==0:
        break

    if cnt>1:
        print()

    a = [[float('inf')]*n for _ in range(n)]
    for i in range(m):
        b, c, d=map(int, input().split())
        b-=1
        c-=1
        a[b][c]=d
        a[c][b]=d

    for i in range(n):
        for j in range(n):
            for k in range(n):
                if max(a[j][i], a[i][k])<a[j][k]:
                    a[j][k]=max(a[j][i], a[i][k])

    print("Case #%d"%(cnt))
    for i in range(q):
        b, c=map(int, input().split())
        b-=1
        c-=1
        
        if a[b][c]==float("inf"):
            print("no path")
        else:
            print(a[b][c])
    cnt+=1