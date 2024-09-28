m,n=map(int, input().split())
g=[]
for i in range(m):
    g.append(list(map(int, input().split())))

dp=[[0 for i in range(n)] for j in range(m)]

dp[0]=g[0]
for i in range(1,m):
    dp[i][0]=dp[i-1][0]+g[i][0]
for i in range(1,n):
    dp[0][i]=dp[0][i-1]+g[0][i]

for i in range(1, m):
    for j in range(1, n):
        dp[i][j]=max(dp[i-1][j], dp[i][j-1])+g[i][j]

print(dp[m-1][n-1])