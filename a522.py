for _ in range(int(input())):
    n=int(input())
    p=int(input())
    P=[int(i) for i in input().split()]
    dp=[0 for i in range(n+1)]
    for i in P:
        for j in range(n,0,-1):
            if j>=i:
                dp[j]=max(dp[j],dp[j-i]+i)
    if dp[n]==n:
        print('YES')
    else:
        print('NO')