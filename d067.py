n=int(input())
s=list(map(int, input().split()))
dp=[0 for i in range(n)]
dp[0]=s[0]
dp[1]=max(dp[0],s[1])
for i in range(2,n):
    dp[i]=max(dp[i-2]+s[i], dp[i-1])
print(dp[-1])