a='0'+input()
b='0'+input()
dp=[[0 for i in range(len(b))] for j in range(len(a))]
for i in range(1, len(a)):
    for j in range(1, len(b)):
        if a[i]==b[j]:
            dp[i][j]=dp[i-1][j-1]+1
        else:
            dp[i][j]=max(dp[i-1][j], dp[i][j-1])
print(dp[-1][-1])