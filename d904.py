c,n=map(int, input().split())
coin=[]
for _ in range(n):
    coin.append(int(input()))
dp=[1000000]*(c+1)
dp[0]=0
for i in range(n):
    for j in range(coin[i],c+1):
        dp[j]=min(dp[j-coin[i]]+1,dp[j])
print(dp[c])