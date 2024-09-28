n,m=map(int, input().split())
node=[[0]*(n+1) for i in range(n+1)]
for _ in range(m):
    a,b=map(int, input().split())
    node[a][b]=1
    node[b][a]=1

for i in range(1, len(node)):
    num=[]
    for j in range(len(node[i])):
        if node[i][j]==1:
            num.append(j)
    print('%d:'%(i), end=' ')
    print(*num)