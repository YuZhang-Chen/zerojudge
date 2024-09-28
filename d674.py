cnt=1
while 1:
    a='0'+input()
    if a=='0#':
        break
    b='0'+input()
    dp=[]
    for i in range(len(a)):
        dp.append([])
        for j in range(len(b)):
            dp[i].append(0)

    for i in range(1,len(a)):
        for j in range(1,len(b)):
            if a[i]==b[j]:
                dp[i][j]=dp[i-1][j-1]+1
            else:
                dp[i][j]=max(dp[i-1][j],dp[i][j-1])
    print('Case #%d: you can visit at most %d cities.'%(cnt,dp[-1][-1]))
    cnt+=1