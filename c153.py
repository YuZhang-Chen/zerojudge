n=int(input())
lst=[[0 for i in range(n)] for j in range(n)]
lst[0][n//2]=1
for k in range(2,n*n+1):
    for i in range(len(lst)):
        if k-1 in lst[i]:
            idx=lst[i].index(k-1)

            if i==0 and idx!=n-1:
                lst[n-1][idx+1]=k

            if idx==n-1 and i!=0:
                lst[i-1][0]=k

            if i==0 and idx==n-1:
                lst[i+1][idx]=k
                
            if i!=0 and idx!=n-1:
                if lst[i-1][idx+1]==0:
                    lst[i-1][idx+1]=k
                else:
                    lst[i+1][idx]=k
for i in lst:
    print(*i)