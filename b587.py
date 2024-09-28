dp=[0]*31
dp[0]=1
dp[2]=3

for i in range(4, len(dp),2):
    dp[i]=4*dp[i-2]-dp[i-4]

while 1:
    n=int(input())
    if n==-1:
        break
    print(dp[n])