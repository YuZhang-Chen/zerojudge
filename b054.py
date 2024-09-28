def f(w,v):
    for i in range(1,len(w)):
        for j in range(1,m+1):
            if j>=w[i]:
                dp[i][j]=max(dp[i-1][j], dp[i-1][j-w[i]]+v[i])
            else:
                dp[i][j]=dp[i-1][j]
    return dp[-1][-1]

m=int(input())
w=[0]
v=[0]
for _ in range(int(input())):
    a,b=map(int, input().split())
    w.append(a)
    v.append(b)
dp=[[0 for i in range(m+1)] for j in range(len(w))]
print(f(w,v))