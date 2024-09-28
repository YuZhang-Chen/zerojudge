price=[1,5,10,25,50]
mxn=30500
dp=[0]*mxn
dp[0]=1
for i in range(len(price)):
    for j in range(price[i], mxn):
        dp[j]+=dp[j-price[i]]

while 1:
    try:
        n=int(input())
        if dp[n]==1:
            print('There is only 1 way to produce %d cents change.'%(n))
        else:
            print('There are %d ways to produce %d cents change.'%(dp[n], n))
    except:
        break





























