cnt=0
while 1:
    try:
        cnt+=1
        n,m=map(int, input().split())
        dp=[[0 for i in range(m)] for j in range(n)]
        a=[]
        for i in range(n):
            a.append(list(map(int, input().split())))
        for j in range(1,m):
            dp[0][j]=dp[0][j-1]+a[0][j]
        for i in range(1,n):
            dp[i][0]=dp[i-1][0]+a[i][0]

        for i in range(1,n):
            for j in range(1,m):
                dp[i][j]=min(dp[i][j-1], dp[i-1][j])+a[i][j]

        print('Case #%d :'%(cnt))
        print(dp[-1][-1])
    except:
        break