dp=[0 for i in range(52)]
dp[0]=1
dp[1]=1
for i in range(2,52):
    dp[i]=dp[i-1]*2+dp[i-2]

n=int(input())
print(dp[n+1])