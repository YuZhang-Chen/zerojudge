n, m = map(int, input().split())
boys = [None]
girls = [None]
while True:
    try:
        b, g = map(int, input().split())
        boys.append(b)
        girls.append(g)
    except:
        break

dp = [[0 for _ in range(m+1)] for _ in range(n+1)]

for i in range(1, n+1):
    dp[i][0] = dp[i-1][0]+boys[i]

for i in range(1, m+1):
    dp[0][i] = dp[0][i-1]+girls[i]

for i in range(1, n+1):
    for j in range(1, m+1):
        dp[i][j] = min(dp[i-1][j]+boys[i+j], dp[i][j-1]+girls[i+j])

print(dp[n][m])