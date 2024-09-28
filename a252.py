a='0'+input()
b='0'+input()
c='0'+input()

dp=[[[0 for i in range(len(c))] for j in range(len(b))] for k in range(len(a))]
for i in range(1,len(a)):
    for j in range(1,len(b)):
        for k in range(1,len(c)):
            if a[i]==b[j] and b[j]==c[k]:
                dp[i][j][k]=dp[i-1][j-1][k-1]+1
            else:
                dp[i][j][k]=max(dp[i-1][j][k],dp[i][j-1][k],dp[i][j][k-1])

print(dp[-1][-1][-1])