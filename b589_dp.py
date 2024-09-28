dp1=[0 for i in range(100)]
while 1:
    n=int(input())
    if n==0:
        break
    x=list(map(int, input().split()))
    dp=dp1.copy()
    for i in range(0,n):
        dp[i+1]=max(dp[i+1], dp[i]+x[i])
        dp[i+2]=max(dp[i+2], dp[i]+2*x[i])
    print(max(dp[n],dp[n+1]))